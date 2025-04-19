import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

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






if __name__ == '__main__':
    db = DB()