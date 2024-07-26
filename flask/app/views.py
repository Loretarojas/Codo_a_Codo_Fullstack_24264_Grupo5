from flask import jsonify, request
from .models import Mariposa


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
    
    mariposa.peligroExtincion = status
    mariposa.migratoria = False
    mariposa.save()
    return jsonify({'message': 'Mariposa actualizada exitosamente'})

def set_mariposa(id):
    return __mariposa(id, True)

def reset_mariposa(id):
    return __mariposa(id, False)
