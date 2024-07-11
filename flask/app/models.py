from app.database import get_db

class Contacto:
    def __init__(self, id=None, nombre=None, correo=None, asunto=None, mensaje=None, informacion=None, pais=None, consultaTipo=None):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.asunto = asunto
        self.mensaje = mensaje
        self.informacion = informacion
        self.pais = pais
        self.asunto = consultaTipo

    @staticmethod
    def __get_contacto_by_query(query):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
    
        contactos = []
        for row in rows:
            contactos.append(
                Contacto(
                    id=row[0],
                    nombre=row[1],
                    correo=row[2],
                    asunto=row[3],
                    mensaje=row[4],
                    informacion=row[5],
                    pais=row[6],
                    consultaTipo=row[7]
                )
            )
        cursor.close()
        return contactos

    @staticmethod
    def get_all_contacto():
        return Contacto.__get_contacto_by_query(
            """
                SELECT * 
                FROM contacto 
                ORDER BY asunto DESC
            """
        )
    @staticmethod
    def eliminar_all_contacto():
        return Contacto.__get_contacto_by_query(
            """
                SELECT * 
                FROM contacto 
                WHERE informacion = false
                ORDER BY nombre DESC
            """
        ) 

  
  
    @staticmethod
    def get_by_id(id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM contacto WHERE id = %s", (id,))

        row = cursor.fetchone()
        cursor.close()

        if row:
            return Contacto(
                id=row[0],
                nombre=row[1],
                correo=row[2],
                asunto=row[3],
                mensaje=row[4],
                informacion=row[5],
                pais=row[6],
                consultaTipo=row[7]
            )
        return None
    
    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id: 
            cursor.execute(
                """
                UPDATE contacto
                SET nombre = %s, correo = %s, mensaje = %s, informacion = %s
                WHERE id = %s
                """,
                (self.nombre, self.correo, self.mensaje, self.informacion, self.id))
        else: 
            cursor.execute(
                """
                INSERT INTO contacto
                (nombre, correo, asunto, mensaje, informacion)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (self.nombre, self.correo, self.asunto, self.mensaje, self.informacion))
            self.id = cursor.lastrowid
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("UPDATE contacto SET informacion = false WHERE id = %s", (self.id,))
        db.commit()
        cursor.close()

    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'correo': self.correo,
            'asunto': self.asunto,
            'mensaje': self.mensaje,
            'informacion': self.informacion,
            'pais': self.pais,

        }