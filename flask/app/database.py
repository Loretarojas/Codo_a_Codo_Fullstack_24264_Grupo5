import os
import psycopg2
from flask import g
from dotenv import load_dotenv

load_dotenv()

DATABASE_CONFIG = {
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'port': os.getenv('DB_PORT', 5432)
}

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(**DATABASE_CONFIG)
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)

def test_connection():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cur = conn.cursor()
    cur.execute('SELECT 1') 
    cur.close()
    conn.close()

def crear_mariposa():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS mariposas (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(50) NOT NULL,
            especie VARCHAR(300) NOT NULL,
            familia VARCHAR(300) NOT NULL,
            nombrecientifico VARCHAR(300) NOT NULL,
            pais VARCHAR(300) NOT NULL,
            peligroextincion BOOLEAN NOT NULL,
            migratoria BOOLEAN NOT NULL
        );
        """
    )
    conn.commit()
    cur.close()
    conn.close()

def create_table_on_startup(app):
    with app.app_context():
        crear_mariposa()
