import os
import pymysql.cursors
from dotenv import load_dotenv

load_dotenv()

# Credentials being pulled in from dotenv file
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


def get_data(sql, conn=connection()):
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
        return result
    except Exception as e:
        input(f"ERROR: {e}")


def update(values, sql, conn=connection(), should_commit=True):
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, dict(values))
            if should_commit:
                conn.commit()
    except Exception as e:
        input(f"ERROR: {e}")
