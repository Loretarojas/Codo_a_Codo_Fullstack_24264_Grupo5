from app.database import get_db

class Mariposas:
    def __init__(self, id=None, familia=None, gen=None, especie=None, ubicacion=None, completada=None, fecha_creacion=None):
        self.id = id
        self.familia = familia
        self.gen = gen
        self.especie = especie
        self.ubicacion = ubicacion
        self.completada = completada
        self.fecha_creacion = fecha_creacion

    @staticmethod
    def __get_mariposas_by_query(query):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        mariposas = []
        for row in rows:
            mariposas.append(
                Mariposas(
                    id=row[0],
                    familia=row[1],
                    gen=row[2],
                    especie=row[3],
                    ubicacion=row[4],
                    completada=row[5],
                    fecha_creacion=row[6]
                )
            )
        cursor.close()
        return mariposas

    @staticmethod
    def get_all_pending():
        return Mariposas.__get_mariposas_by_query(
            """ 
            SELECT * 
            FROM mariposas 
            WHERE completada = false
            ORDER BY fecha_creacion DESC
            """
        )

    @staticmethod
    def get_all_completed():
        return Mariposas.__get_mariposas_by_query(
            """ 
            SELECT *   
            FROM mariposas 
            WHERE completada = true
            ORDER BY fecha_creacion DESC
            """
        )

    @staticmethod
    def get_by_id(id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM mariposas WHERE id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()

        if row:
            return Mariposas(
                id=row[0],
                familia=row[1],
                gen=row[2],
                especie=row[3],
                ubicacion=row[4],
                completada=row[5],
                fecha_creacion=row[6]
            )
        return None

    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id:  # Actualizar
            cursor.execute(
                """
                UPDATE mariposas
                SET familia = %s, gen = %s, especie = %s, ubicacion = %s, completada = %s, fecha_creacion = %s
                WHERE id = %s
                """,
                (self.familia, self.gen, self.especie, self.ubicacion, self.completada, self.fecha_creacion, self.id)
            )
        else:  # Crear
            cursor.execute(
                """
                INSERT INTO mariposas
                (familia, gen, especie, ubicacion, completada, fecha_creacion)
                VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;
                """,
                (self.familia, self.gen, self.especie, self.ubicacion, self.completada, self.fecha_creacion)
            )
            self.id = cursor.fetchone()[0]
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM mariposas WHERE id = %s", (self.id,))
        db.commit()
        cursor.close()

    def serialize(self):
        return {
            'id': self.id,
            'familia': self.familia,
            'gen': self.gen,
            'especie': self.especie,
            'ubicacion': self.ubicacion,
            'completada': self.completada,
            'fecha_creacion': self.fecha_creacion.strftime('%Y-%m-%d'),
        }
