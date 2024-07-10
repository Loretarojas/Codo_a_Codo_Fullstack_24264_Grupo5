from . import db

class Contacto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    asunto = db.Column(db.String(100), nullable=False)
    mensaje = db.Column(db.Text, nullable=False)
    info = db.Column(db.Boolean, default=False)
    pais = db.Column(db.String(50), nullable=False)
    consultaTipo = db.Column(db.String(50), nullable=False)
