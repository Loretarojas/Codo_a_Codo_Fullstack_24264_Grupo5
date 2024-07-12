from flask import g
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
    def get_all_mariposa():
        db = get_db()
        cur = db.cursor()
        cur.execute("SELECT id, nombre, especie, familia, nombreCientifico, pais, peligroExtincion, migratoria FROM Mariposa;")
        rows = cur.fetchall()
        cur.close()
        return [Mariposa(*row) for row in rows]
    
    @staticmethod
    def eliminar_all_mariposa(id):
        db = get_db()
        cur = db.cursor()
        cur.execute("DELETE FROM Mariposa WHERE id=%s;", (id,))
        db.commit()
        cur.execute("SELECT id, nombre, especie, familia, nombreCientifico, pais, peligroExtincion, migratoria FROM Mariposa;")
        rows = cur.fetchall()
        cur.close()
        return [Mariposa(*row) for row in rows]


    @staticmethod
    def get_by_id(id):
        db = get_db()
        cur = db.cursor()
        cur.execute("SELECT id, nombre, especie, familia, nombreCientifico, pais, peligroExtincion, migratoria FROM Mariposa WHERE id=%s;", (id,))
        row = cur.fetchone()
        cur.close()
        if row:
            return Mariposa(*row)
        return None

    def save(self):
        db = get_db()
        cur = db.cursor()
        if self.id is None:
            cur.execute("""
                INSERT INTO Mariposa (nombre, especie, familia, nombreCientifico, pais, peligroExtincion, migratoria)
                VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id;
            """, (self.nombre, self.especie, self.familia, self.nombreCientifico, self.pais, self.peligroExtincion, self.migratoria))
            self.id = cur.fetchone()[0]
        else:
            cur.execute("""
                UPDATE Mariposa SET nombre=%s, especie=%s, familia=%s, nombreCientifico=%s, pais=%s, peligroExtincion=%s, migratoria=%s
                WHERE id=%s;
            """, (self.nombre, self.especie, self.familia, self.nombreCientifico, self.pais, self.peligroExtincion, self.migratoria, self.id))
        db.commit()
        cur.close()


    def delete(self):
        db = get_db()
        cur = db.cursor()
        cur.execute("DELETE FROM Mariposa WHERE id=%s;", (self.id,))
        db.commit()
        cur.close()
    
    
    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'especie': self.especie,
            'familia': self.familia,
            'nombreCientifico': self.nombreCientifico,
            'pais': self.pais,
            'peligroExtincion': self.peligroExtincion,
            'migratoria': self.migratoria
        }

    

   

    

    

   
