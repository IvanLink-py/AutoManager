import datetime

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from typing import List, Tuple
import models

class DB:
    DB_NAME = "AutoManager"
    instance = None

    def __init__(self):
        try:
            self.conn = psycopg2.connect(dbname=self.DB_NAME, user="postgres", host="192.168.2.164", password="root")
        except:
            self.create_db()
            self.conn = psycopg2.connect(dbname="postgres", user="postgres", host="192.168.2.164", password="root")

        self.instance = self

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
    def send_trip(bus, driver, schedule) -> bool:
        pass
    
    @staticmethod
    def end_trip(trip: models.Trip, success: bool) -> bool:
        pass

if __name__ == '__main__':
    db = DB()