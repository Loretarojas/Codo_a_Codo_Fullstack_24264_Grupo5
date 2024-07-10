from flask import Blueprint, request, jsonify
from .models import Contacto
from . import db

main = Blueprint('main', __name__)

@main.route('/contacto', methods=['POST'])
def crear_contacto():
    data = request.json
    nuevo_contacto = Contacto(
        nombre=data['nombre'],
        correo=data['correo'],
        asunto=data['asunto'],
        mensaje=data['mensaje'],
        info=data.get('info', False),
        pais=data['pais'],
        consultaTipo=data['consultaTipo']
    )
    db.session.add(nuevo_contacto)
    db.session.commit()
    return jsonify({'message': 'Contacto creado exitosamente'}), 201

@main.route('/contacto', methods=['GET'])
def obtener_contactos():
    contactos = Contacto.query.all()
    return jsonify([{
        'id': contacto.id,
        'nombre': contacto.nombre,
        'correo': contacto.correo,
        'asunto': contacto.asunto,
        'mensaje': contacto.mensaje,
        'info': contacto.info,
        'pais': contacto.pais,
        'consultaTipo': contacto.consultaTipo
    } for contacto in contactos]), 200

@main.route('/contacto/<int:id>', methods=['GET'])
def obtener_contacto(id):
    contacto = Contacto.query.get_or_404(id)
    return jsonify({
        'id': contacto.id,
        'nombre': contacto.nombre,
        'correo': contacto.correo,
        'asunto': contacto.asunto,
        'mensaje': contacto.mensaje,
        'info': contacto.info,
        'pais': contacto.pais,
        'consultaTipo': contacto.consultaTipo
    }), 200

@main.route('/contacto/<int:id>', methods=['PUT'])
def actualizar_contacto(id):
    data = request.json
    contacto = Contacto.query.get_or_404(id)
    contacto.nombre = data['nombre']
    contacto.correo = data['correo']
    contacto.asunto = data['asunto']
    contacto.mensaje = data['mensaje']
    contacto.info = data.get('info', contacto.info)
    contacto.pais = data['pais']
    contacto.consultaTipo = data['consultaTipo']

    db.session.commit()
    return jsonify({'message': 'Contacto actualizado exitosamente'}), 200

@main.route('/contacto/<int:id>', methods=['DELETE'])
def eliminar_contacto(id):
    contacto = Contacto.query.get_or_404(id)
    db.session.delete(contacto)
    db.session.commit()
    return jsonify({'message': 'Contacto eliminado exitosamente'}), 200
