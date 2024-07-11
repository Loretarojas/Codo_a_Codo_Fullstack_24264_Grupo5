from app.database import get_db

class Mariposa:
    def __init__(self, id=None, nombre=None, especie=None, familia=None, nombreCientifico=None, pais=None, peligroExtincion=None, migratoria=None):
        self.id = id
        self.nombre = nombre
        self.especie = especie
        self.familia = familia
        self.nombreCientifico = nombreCientifico
        self.pais = pais
        self.peligroExtincion = peligroExtincion
        self.migratoria = migratoria


    @staticmethod
    def __get_mariposa_by_query(query):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
    
        mariposas = []
        for row in rows:
            mariposas.append(
                Mariposa(
                    id=row[0],
                    nombre=row[1],
                    especie=row[2],
                    familia=row[3],
                    nombreCientifico=row[4],
                    pais=row[5],
                    peligroExtincion=row[6],
                    migratoria=row[7]
                )
            )
        cursor.close()
        return mariposas

    @staticmethod
    def get_all_mariposa():
        return Mariposa.__get_mariposa_by_query(
            """
                SELECT * 
                FROM mariposa 
                ORDER BY especie DESC
            """
        )
    @staticmethod
    def eliminar_all_mariposa():
        return Mariposa.__get_mariposa_by_query(
            """
                SELECT * 
                FROM mariposa 
                WHERE peligroExtincion = false
                ORDER BY nombre DESC
            """
        ) 

  
    @staticmethod
    def get_by_id(id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM mariposa WHERE id = %s", (id,))

        row = cursor.fetchone()
        cursor.close()

        if row:
            return Mariposa(
                id=row[0],
                nombre=row[1],
                especie=row[2],
                familia=row[3],
                nombreCientifico=row[4],
                pais=row[5],
                peligroExtincion=row[6],
                migratoria=row[7]
            )
        return None
    
    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id: 
            cursor.execute(
                """
                UPDATE mariposa
                SET nombre = %s, especie = %s, familia = %s, nombreCientifico = %s
                WHERE id = %s
                """,
                (self.nombre, self.especie, self.familia, self.nombreCientifico, self.id))
        else: 
            cursor.execute(
                """
                INSERT INTO mariposa
                (nombre, especie, familia, nombreCientifico, peligroExtincion)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (self.nombre, self.especie, self.familia, self.nombreCientifico, self.peligroExtincion))
            self.id = cursor.lastrowid
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("UPDATE mariposa SET peligroExtincion = false WHERE id = %s", (self.id,))
        db.commit()
        cursor.close()

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