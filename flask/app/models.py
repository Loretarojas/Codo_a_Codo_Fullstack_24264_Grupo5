from flask import g
import psycopg2
from .database import get_db

class Mariposa:
    def __init__(self, id, nombre, especie, familia, nombreCientifico, pais, peligroExtincion, migratoria):
        self.id = id
        self.nombre = nombre
        self.especie = especie
        self.familia = familia
        self.nombreCientifico = nombreCientifico
        self.pais = pais
        self.peligroExtincion = peligroExtincion
        self.migratoria = migratoria

    @staticmethod
    def eliminar_all_mariposa(id):
        db = get_db()
        cur = db.cursor()
        cur.execute("DELETE FROM mariposas WHERE id=%s;", (id,))
        db.commit()
        cur.execute("SELECT id, nombre, especie, familia, nombrecientifico, pais, peligroextincion, migratoria FROM mariposas;")
        rows = cur.fetchall()
        cur.close()
        return [Mariposa(*row) for row in rows]

    @staticmethod
    def get_all_mariposa():
        with get_db() as db:
            with db.cursor() as cur:
                cur.execute("SELECT * FROM mariposas;")
                rows = cur.fetchall()
                return [Mariposa(*row) for row in rows]

    @staticmethod
    def get_by_id(id):
        with get_db() as db:
            with db.cursor() as cur:
                cur.execute("SELECT * FROM mariposas WHERE id = %s;", (id,))
                row = cur.fetchone()
                return Mariposa(*row) if row else None

    def save(self):
        with get_db() as db:
            with db.cursor() as cur:
                if self.id is None:
                    cur.execute("""
                        INSERT INTO mariposas (nombre, especie, familia, nombrecientifico, pais, peligroextincion, migratoria)
                        VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id;
                    """, (self.nombre, self.especie, self.familia, self.nombreCientifico, self.pais, self.peligroExtincion, self.migratoria))
                    self.id = cur.fetchone()[0]
                else:
                    cur.execute("""
                        UPDATE mariposas SET nombre=%s, especie=%s, familia=%s, nombrecientifico=%s, pais=%s, peligroextincion=%s, migratoria=%s
                        WHERE id=%s;
                    """, (self.nombre, self.especie, self.familia, self.nombreCientifico, self.pais, self.peligroExtincion, self.migratoria, self.id))

    def delete(self):
        with get_db() as db:
            with db.cursor() as cur:
                cur.execute("DELETE FROM mariposas WHERE id = %s;", (self.id,))
