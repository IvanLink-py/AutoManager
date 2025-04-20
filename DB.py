import datetime

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2.extensions import adapt, register_adapter, AsIs
from typing import List, Tuple
import dataclasses
import models

class DB:
    DB_NAME = "AutoManager"
    instance = None

    def __init__(self):
        try:
            self.conn = psycopg2.connect(dbname=self.DB_NAME, user="postgres", host="192.168.2.164", password="root")
            self.conn.autocommit = True
        except:
            self.create_db()
            self.conn = psycopg2.connect(dbname=self.DB_NAME, user="postgres", host="192.168.2.164", password="root")
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
            if f == "_id":
                continue
            q_fields.append(adapt(model[f]).getquoted().decode())

        return AsIs(f"{', '.join(q_fields)}")

    @staticmethod
    def get_fields(model):
        model = dataclasses.asdict(model)
        keys = []
        for k in model:
            if k == "_id":
                continue
            keys.append(k)
        return ", ".join(keys)

    @staticmethod
    def create_db():
        conn = psycopg2.connect(dbname="postgres", user="postgres", host="192.168.2.164", password="root")
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
        pass

    @staticmethod
    def save_route(route: models.Route) -> bool:
        pass

    @staticmethod
    def get_schedule() -> List[models.Schedule]:
        pass

    @staticmethod
    def get_next_trips() -> List[Tuple[datetime.time, models.Schedule]]:
        pass

    @staticmethod
    def send_trip(bus: models.Bus, driver: models.Driver, schedule: models.Schedule) -> bool:
        pass

    @staticmethod
    def get_drivers() -> List[models.Driver]:
        pass

    @staticmethod
    def get_busses() -> List[models.Bus]:
        pass

    @staticmethod
    def create_driver(driver: models.Driver):
        with DB.instance.conn.cursor() as curs:
            sql = f"INSERT INTO driver ({DB.instance.get_fields(driver)}) VALUES (%s)"
            curs.execute(sql, (driver, ))

    @staticmethod
    def create_bus(bus: models.Bus) -> bool:
        pass
    
    @staticmethod
    def end_trip(trip: models.Trip, success: bool) -> bool:
        pass

if __name__ == '__main__':
    db = DB()