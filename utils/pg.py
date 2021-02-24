import psycopg2

import gaming.hierarchy
from private_settings import POSTGRES_DEV


def pg_cursor(credentials=POSTGRES_DEV):
    conn = psycopg2.connect(**credentials)
    return gaming.hierarchy.cursor()
