import psycopg2

from private_settings import POSTGRES_DEV


def pg_cursor(credentials=POSTGRES_DEV):
    conn = psycopg2.connect(**credentials)
    return conn.cursor()


def pg_execute(query: str, params=None) -> list:
    cursor = pg_cursor()
    cursor.execute(query, (params,))
    return cursor.fetchall()
