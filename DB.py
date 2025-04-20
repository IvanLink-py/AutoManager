import datetime
import configparser
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT, NoneAdapter
from psycopg2.extensions import adapt, register_adapter, AsIs
from typing import List, Tuple
import dataclasses
import models
from os import path
import sys


class DB:
    DB_NAME = "AutoManager"
    instance = None

    def __init__(self):
        cfg = configparser.ConfigParser()
        if not path.exists('config.ini'):
            cfg['DataBase'] = {
                "IP": "127.0.0.1",
                "user": "postgres",
                "password": "postgres"
            }

            with open('config.ini', 'w') as configfile:
                cfg.write(configfile)

            import sys
            from PySide6 import QtWidgets
            app = QtWidgets.QApplication(sys.argv)
            a = QtWidgets.QMessageBox.information(None, 'Обновление конфигурации',
                                                  "Не удалось найти конфигурационный файл 'config.ini'\nЗаполните данные для подкючения в файл.",
                                                  QtWidgets.QMessageBox.Ok)
            sys.exit(0)

        else:
            cfg.read('config.ini')

        try:
            self.conn = psycopg2.connect(dbname=self.DB_NAME, user=cfg['DataBase']['user'], host=cfg['DataBase']['IP'],
                                         password=cfg['DataBase']['password'])
            self.conn.autocommit = True
        except:
            self.create_db()
            self.conn = psycopg2.connect(dbname=self.DB_NAME, user=cfg['DataBase']['user'], host=cfg['DataBase']['IP'],
                                         password=cfg['DataBase']['password'])

            self.conn.autocommit = True

        register_adapter(models.Stop, self.adapt_model)
        register_adapter(models.Route, self.adapt_model)
        register_adapter(models.Bus, self.adapt_model)
        register_adapter(models.Driver, self.adapt_model)
        register_adapter(models.Schedule, self.adapt_model)
        register_adapter(models.Trip, self.adapt_model)

        DB.instance = self

    @staticmethod
    def adapt_model(model):
        model = dataclasses.asdict(model)
        q_fields = []
        for f in model:
            if (f == "_id") or (type(model[f]) == list):
                continue
            ad = adapt(model[f])
            if type(model[f]) != bool and type(model[f]) != int and type(ad) != NoneAdapter and type(
                    model[f]) != datetime.datetime:
                ad.prepare(DB.instance.conn)
            q_fields.append(ad.getquoted().decode("utf-8"))

        return AsIs(f"{', '.join(q_fields)}")

    @staticmethod
    def get_fields(model):
        model = dataclasses.asdict(model)
        keys = []
        for k in model:
            if (k == "_id") or (type(model[k]) == list):
                continue
            keys.append(k)
        return ", ".join(keys)

    @staticmethod
    def create_db():
        cfg = configparser.ConfigParser()
        cfg.read('config.ini')
        try:
            conn = psycopg2.connect(dbname="postgres", host=cfg['DataBase']['IP'], password=cfg['DataBase']['password'])
        except psycopg2.OperationalError:
            import sys
            from PySide6 import QtWidgets
            app = QtWidgets.QApplication(sys.argv)
            a = QtWidgets.QMessageBox.critical(None, 'Ошибка подключения',
                                               "Не удалось подключиться к БД\nПроверьте config.ini",
                                               QtWidgets.QMessageBox.Ok)
            sys.exit(0)

        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute("""

CREATE DATABASE "AutoManager"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LOCALE_PROVIDER = 'libc'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False; """)

        cur.close()
        conn.close()

        conn = psycopg2.connect(dbname=DB.DB_NAME, user="postgres", host="192.168.2.164", password="root")
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute(open("schema.sql", "r", encoding="utf8").read())

        cur.close()
        conn.close()

    @staticmethod
    def get_routes() -> List[models.Route]:
        stops = DB.get_stops()
        routes = {}
        route_stops = []

        with DB.instance.conn.cursor() as curs:
            sql = f"SELECT * FROM route"
            curs.execute(sql)
            for data in curs.fetchall():
                routes[data[0]] = models.Route(data[0], data[1], data[2], [])

        with DB.instance.conn.cursor() as curs:
            sql = f'SELECT * FROM route_stop ORDER BY "index" ASC'
            curs.execute(sql)
            for data in curs.fetchall():
                route_stops.append({"route_id": data[1], "stop_id": data[2]})

        for rs in route_stops:
            routes[rs["route_id"]].stops.append(filter(lambda s: s._id == rs["stop_id"], stops).__next__())

        return list(routes.values())

    @staticmethod
    def save_route(route: models.Route):
        if route is None:
            return

        if route._id != -1:
            with DB.instance.conn.cursor() as curs:
                sql = f"DELETE FROM route_stop WHERE route_id = %s"
                curs.execute(sql, (route._id,))

            with DB.instance.conn.cursor() as curs:
                sql = f"DELETE FROM route WHERE id = %s "
                curs.execute(sql, (route._id,))

        with DB.instance.conn.cursor() as curs:
            sql = f"INSERT INTO route ({DB.instance.get_fields(route)}) VALUES (%s)"
            curs.execute(sql, (route,))

        with DB.instance.conn.cursor() as curs:
            sql = f"SELECT * FROM route WHERE name = %s LIMIT 1"
            curs.execute(sql, (route.name,))
            route._id = curs.fetchone()[0]

        with DB.instance.conn.cursor() as curs:
            for i, stop in enumerate(route.stops):
                sql = 'INSERT INTO route_stop (route_id, stop_id, "index") VALUES (%s, %s, %s)'
                curs.execute(sql, (route._id, stop._id, i))

    @staticmethod
    def get_schedule() -> List[models.Schedule]:
        with DB.instance.conn.cursor() as curs:
            sql = f"SELECT * FROM schedule order by start_time"
            curs.execute(sql)
            result = []
            for data in curs.fetchall():
                result.append(models.Schedule(*data))

        routes = DB.get_routes()
        for s in result:
            s.route = filter(lambda r: r._id == s.route, routes).__next__()

        return result

    @staticmethod
    def save_schedule(schedule: models.Schedule):
        if schedule is None:
            return
        with DB.instance.conn.cursor() as curs:
            sql = f"INSERT INTO schedule ({DB.instance.get_fields(schedule)}) VALUES (%s, %s, %s)"
            curs.execute(sql, (schedule.start_time, schedule.week_days, schedule.route._id))

    @staticmethod
    def get_next_trips() -> List[models.Schedule]:
        schedules = DB.get_schedule()
        next_trips = []

        if datetime.date.today().weekday() == 0:
            td = "ПН"
        elif datetime.date.today().weekday() == 1:
            td = "ВТ"
        elif datetime.date.today().weekday() == 2:
            td = "СР"
        elif datetime.date.today().weekday() == 3:
            td = "ЧТ"
        elif datetime.date.today().weekday() == 4:
            td = "ПТ"
        elif datetime.date.today().weekday() == 5:
            td = "СБ"
        else:
            td = "ВС"

        for sch in schedules:
            if td.lower() in sch.week_days.lower():
                next_trips.append(sch)

        with DB.instance.conn.cursor() as curs:
            sql = f"SELECT * FROM trip where DATE(send_time) = CURRENT_DATE "
            curs.execute(sql)
            td_trips = []
            for data in curs.fetchall():
                td_trips.append(models.Trip(*data))

        for td_trip in td_trips:
            next_trips.remove(filter(lambda t: td_trip.schedule_id == t._id, next_trips).__next__())

        return next_trips

    @staticmethod
    def send_trip(bus: models.Bus, driver: models.Driver, schedule: models.Schedule):
        if (bus is None) or (driver is None) or (schedule is None):
            return
        with DB.instance.conn.cursor() as curs:
            trip = models.Trip(-1, bus._id, driver._id, schedule._id, None, datetime.datetime.now())
            sql = f"INSERT INTO trip ({DB.instance.get_fields(trip)}) VALUES (%s)"
            curs.execute(sql, (trip,))

    @staticmethod
    def get_actual_trips() -> List[models.Trip]:
        with DB.instance.conn.cursor() as curs:
            sql = f"SELECT * FROM trip where success IS NULL"
            curs.execute(sql)
            result = []
            for data in curs.fetchall():
                result.append(models.Trip(*data))

        schedules = DB.get_schedule()
        for s in result:
            s.schedule_id = filter(lambda r: r._id == s.schedule_id, schedules).__next__()

        return result

    @staticmethod
    def get_drivers() -> List[models.Driver]:
        with DB.instance.conn.cursor() as curs:
            sql = f"SELECT * FROM driver"
            curs.execute(sql)
            result = []
            for data in curs.fetchall():
                result.append(models.Driver(*data))

        return result

    @staticmethod
    def get_stops() -> List[models.Stop]:
        with DB.instance.conn.cursor() as curs:
            sql = f"SELECT * FROM stop"
            curs.execute(sql)
            result = []
            for data in curs.fetchall():
                result.append(models.Stop(*data))

        return result

    @staticmethod
    def create_stop(stop: models.Stop):
        if stop is None:
            return
        with DB.instance.conn.cursor() as curs:
            sql = f"INSERT INTO stop ({DB.instance.get_fields(stop)}) VALUES (%s)"
            curs.execute(sql, (stop,))

    @staticmethod
    def get_busses() -> List[models.Bus]:
        with DB.instance.conn.cursor() as curs:
            sql = f"SELECT * FROM bus"
            curs.execute(sql)
            result = []
            for data in curs.fetchall():
                result.append(models.Bus(*data))

        return result

    @staticmethod
    def create_driver(driver: models.Driver):
        if driver is None:
            return
        with DB.instance.conn.cursor() as curs:
            sql = f"INSERT INTO driver ({DB.instance.get_fields(driver)}) VALUES (%s)"
            curs.execute(sql, (driver,))

    @staticmethod
    def create_bus(bus: models.Bus):
        if bus is None:
            return
        with DB.instance.conn.cursor() as curs:
            sql = f"INSERT INTO bus ({DB.instance.get_fields(bus)}) VALUES (%s)"
            curs.execute(sql, (bus,))

    @staticmethod
    def end_trip(trip: models.Trip, success: bool) -> bool:
        with DB.instance.conn.cursor() as curs:
            sql = f"UPDATE trip SET success=%s WHERE id=%s;"
            curs.execute(sql, (success, trip._id))


if __name__ == '__main__':
    db = DB()
