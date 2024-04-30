import psycopg2
from config import load_config

def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            print('PostgreSQL database version:')
            cur = conn.cursor()
            cur.execute('SELECT version()')
            db_ver = cur.fetchall()
            print(db_ver)
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == '__main__':
    config = load_config()
    connect(config)