from flask import jsonify, request
from .models import Contacto


def get_completed_contacto():
    contactos = Contacto.get_all_contacto()
    return jsonify([contacto.serialize() for contacto in contactos])

def eliminar_contacto(id):
    contactos = Contacto.eliminar_all_contacto(id)
    return jsonify([contacto.serialize() for contacto in contactos])

def get_contacto(id):
    contacto = Contacto.get_by_id(id)
    if not contacto:
        return jsonify({'message': 'contacto not found'}), 404
    return jsonify(contacto.serialize())

def crear_contacto():
    data = request.json
    nuevo_contacto = Contacto(
        nombre=data['nombre'],
        especie=data['especie'],
        familia=data['familia'],
        nombreCientifico=data['nombreCientifico'],
        pais=data['pais'],
        peligroExtincion=data('peligroExtincion', False),
        migratoria=data['migratoria']
    )
    nuevo_contacto.save()
    return jsonify({'message': 'Contacto creado exitosamente'}), 201


def actualizar_contacto(id):
   contacto = Contacto.get_by_id(id)
   if not contacto:
        return jsonify({'message': 'contacto not found'}), 404
   data = request.json
   contacto.nombre = data['nombre'] 
   contacto.especie = data['especie']
   contacto.save()
   return jsonify({'message': 'contacto updated successfully'})


def eliminar_contacto(id):
    contacto = Contacto.get_by_id(id)
    if not contacto:
        return jsonify({'message': 'Contacto not found'}), 404
    
    contacto.delete()
    return jsonify({'message': 'Contacto deleted successfully'})

def __contacto(id, status):
    contacto = Contacto.get_by_id(id)
    if not Contacto:
        return jsonify({'message': 'Contacto not found'}), 404

    contacto.especie = status
    contacto.save()
    return jsonify({'message': 'Contacto updated successfully'})

def set_contacto(id):
    return __contacto(id, True)

def reset_contacto(id):
    return __contacto(id, False)