from app.database import get_db

class Mariposas:
    def __init__(self, id_mariposas=None, familia=None, gen=None, especie=None, ubicacion=None, completada=None, fecha_creacion=None):
        self.id_mariposas = id_mariposas
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
                    id_mariposas=row[0],
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
                FROM  mariposas 
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
                WHERE  completada = true
                ORDER BY fecha_creacion DESC
            """
        )
    

    @staticmethod
    def get_by_id(id_mariposas):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM mariposas WHERE id = %s", (id_mariposas,))
        row = cursor.fetchone()
        cursor.close()
        
        if row:
            return Mariposas(
                id_mariposas=row[0],
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
        if self.id_mariposas: # Actualizar 
            cursor.execute(
                """
                UPDATE mariposas
                SET familia = %s, gen = %s, especie = %s, completada = %s
                WHERE id = %s
                """,
                (self.familia, self.gen, self.especie, self.completada, self.id_mariposas))
        else: # Crear 
            cursor.execute(
                """
                INSERT INTO mariposas
                (familia, gen, especie, ubicacion, completada, fecha_creacion)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (self.familia, self.gen, self.especie, self.ubicacion, self.completada, self.fecha_creacion))
            self.id_mariposas = cursor.lastrowid
        db.commit()
        cursor.close()


    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("UPDATE tareas SET activa = false WHERE id = %s", (self.id_mariposas,))
        db.commit()
        cursor.close()

    def serialize(self):
            return {
                'id': self.id_mariposas,
                'familia': self.familia,
                'gen': self.gen,
                'especie': self.especie,
                'ubicacion': self.ubicacion,
                'completada': self.completada,
                'fecha_creacion': self.fecha_creacion.strftime('%Y-%m-%d'),
            }
