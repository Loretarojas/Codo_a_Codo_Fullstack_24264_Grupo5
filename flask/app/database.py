import os
import psycopg2
from flask import g
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la base de datos usando variables de entorno
DATABASE_CONFIG = {
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'port': os.getenv('DB_PORT', 5432)
}

# Función para obtener la conexión a la base de datos
def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(**DATABASE_CONFIG)
    return g.db

# Función para cerrar la conexión a la base de datos
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# Función para inicializar la aplicación con el manejo de la base de datos
def init_app(app):
    app.teardown_appcontext(close_db)

def test_connection():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cur = conn.cursor()
    conn.commit()
    cur.close()
    conn.close()

def create_table_mariposas():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS mariposas (
            id SERIAL PRIMARY KEY,
            familia VARCHAR(50) NOT NULL,
            gen VARCHAR(300) NOT NULL,
            especie VARCHAR(300) NOT NULL,
            ubicacion VARCHAR(300) NOT NULL,
            completada BOOLEAN NOT NULL,
            fecha_creacion DATE NOT NULL
        );
        """
    )
    conn.commit()
    cur.close()
    conn.close()

def insertar_mariposas(familia, gen, especie, ubicacion, completada, fecha_creacion):
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO mariposas
            (familia, gen, especie, ubicacion, completada, fecha_creacion)
            VALUES (%s, %s, %s, %s, %s, %s);
        """,
        (familia, gen, especie, ubicacion, completada, fecha_creacion)
    )
    conn.commit()
    cur.close()
    conn.close()
