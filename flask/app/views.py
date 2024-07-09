from flask import jsonify, request
from app.models import Mariposas
from datetime import date

def index():
    return jsonify(
        {
            'mensaje': 'FlutterSearch'
        }
    )

def get_pending_mariposas():
    mariposas = Mariposas.get_all_pending()
    return jsonify([mariposa.serialize() for mariposa in mariposas])

def get_completed_mariposas():
    mariposas = Mariposas.get_all_completed()
    return jsonify([mariposa.serialize() for mariposa in mariposas])

def get_mariposas(mariposas_id):
    mariposas = Mariposas.get_by_id(mariposas_id)
    if not mariposas:
        return jsonify({'message': 'Query not found'}), 404
    return jsonify(mariposas.serialize())

def create_consulta():
    data = request.json
    new_mariposas = Mariposas(
        familia=data['familia'],
        gen=data['gen'],
        especie=data['especie'],
        ubicacion=data['ubicacion'],
        completada=False,
        fecha_creacion=date.today().strftime('%Y-%m-%d')
    )
    new_mariposas.save()
    return jsonify({'message': 'Query created successfully'}), 201

def update_consulta(mariposas_id):
    mariposas = Mariposas.get_by_id(mariposas_id)
    if not mariposas:
        return jsonify({'message': 'Query not found'}), 404
    
    data = request.json
    mariposas.familia = data['familia']
    mariposas.gen = data['gen']
    mariposas.especie = data['especie']
    mariposas.ubicacion = data['ubicacion']
    mariposas.completada = data.get('completada', mariposas.completada)
    mariposas.fecha_creacion = data.get('fecha_creacion', mariposas.fecha_creacion)
    mariposas.save()
    return jsonify({'message': 'Query updated successfully'})

def delete_mariposas(mariposas_id):
    mariposas = Mariposas.get_by_id(mariposas_id)
    if not mariposas:
        return jsonify({'message': 'Mariposa not found'}), 404
   
    mariposas.delete()
    return jsonify({'message': 'Mariposa deleted successfully'})

def __complete_mariposas(mariposas_id, status):
    mariposas = Mariposas.get_by_id(mariposas_id)
    if not mariposas:
        return jsonify({'message': 'Mariposa not found'}), 404

    mariposas.completada = status
    mariposas.save()
    return jsonify({'message': 'Mariposas updated successfully'})

def set_complete_mariposas(mariposas_id):
    return __complete_mariposas(mariposas_id, True)

def reset_complete_mariposas(mariposas_id):
    return __complete_mariposas(mariposas_id, False)
