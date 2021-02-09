import os
import pymysql.cursors
from dotenv import load_dotenv

load_dotenv()


HOST = os.environ.get("MYSQL_HOST")
USER = os.environ.get("MYSQL_USER")
PASSWORD = os.environ.get("MYSQL_PASS")
DB = os.environ.get("MYSQL_DB")
PORT = int(os.environ.get("MYSQL_PORT"))


def connection():
    return pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        db=DB,
        port=PORT,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )


def get_data(table_name, conn=connection()):
    with conn.cursor() as cursor:
        sql = f"SELECT * FROM {table_name}"
        cursor.execute(sql)
        result = cursor.fetchall()
    return result


def update(table_name, column1, column2, conn=connection()):
    with conn.cursor() as cursor:
        sql = f"INSERT INTO {table_name}({column1}, {column2})
        cursor.execute(sql, values)
    return conn.commit()