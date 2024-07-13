from flask import jsonify, request
from .models import Mariposa

def index():
    return jsonify({'message': 'Bienvenido a la API de Mariposas'})

def get_completed_mariposa():
    mariposas = Mariposa.get_all_mariposa()
    return jsonify([mariposa.serialize() for mariposa in mariposas])

def get_mariposa(id):
    mariposa = Mariposa.get_by_id(id)
    if not mariposa:
        return jsonify({'message': 'Mariposa no encontrada'}), 404
    return jsonify(mariposa.serialize())

def crear_mariposa():
    data = request.json
    nuevo_mariposa = Mariposa(
        nombre=data['nombre'],
        especie=data['especie'],
        familia=data['familia'],
        nombreCientifico=data['nombreCientifico'],
        pais=data['pais'],
        peligroExtincion=False,
        migratoria=False
    )
    nuevo_mariposa.save()
    return jsonify({'message': 'Mariposa creada exitosamente'}), 201

def actualizar_mariposa(id):
    mariposa = Mariposa.get_by_id(id)
    if not mariposa:
        return jsonify({'message': 'Mariposa no encontrada'}), 404
    data = request.json
    mariposa.nombre = data['nombre']
    mariposa.especie = data['especie']
    mariposa.familia = data['familia']
    mariposa.nombreCientifico = data['nombreCientifico']
    mariposa.pais = data['pais']
    mariposa.peligroExtincion = False
    mariposa.migratoria = False
    mariposa.save()
    return jsonify({'message': 'Mariposa actualizada exitosamente'})

def eliminar_mariposa(id):
    mariposa = Mariposa.get_by_id(id)
    if not mariposa:
        return jsonify({'message': 'Mariposa no encontrada'}), 404
    mariposa.delete()
    return jsonify({'message': 'Mariposa eliminada exitosamente'})

def __mariposa(id, status):
    mariposa = Mariposa.get_by_id(id)
    if not mariposa:
        return jsonify({'message': 'Mariposa no encontrada'}), 404
    mariposa.migratoria = status
    mariposa.save()
    return jsonify({'message': 'Mariposa actualizada exitosamente'})

def set_mariposa(id):
    return __mariposa(id, True)

def reset_mariposa(id):
    return __mariposa(id, False)
