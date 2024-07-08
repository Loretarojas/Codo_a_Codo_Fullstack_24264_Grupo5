from flask import jsonify, request

def index():
    return jsonify(
        {
            'mensaje': 'FlutterSearch'
        }
    )

def get_pending_fluttersearch():
    fluttersearch = [
       {
           "id":1,
            "familia":"Acrolophidae",
            "gen":"Acrolophus",
            "especie":"nr. cressoni",
            "ubicacion":"Mexico",
            'completada': False
        },
        {
            "id":2,
            "familia":"Roeslerstammiidae",
            "gen":"Amphithera",
            "especie":"heteroleuca",
            "ubicacion":"Australia",
            'completada': False
        },
    ]
    return jsonify(fluttersearch)

def get_mariposas(mariposas_id):
    mariposas = {
        'id':mariposas_id,
    }
    return jsonify(mariposas)

def create_consulta():
#datos recibidos en formato json
    data = request.json
    return jsonify({'message': 'Query created successfully','data':data}), 201

def update_consulta(mariposas_id):
    data = request.json
    return jsonify({'message': 'Query updated successfully','data':data, 'id':mariposas_id}), 200

def set_complete_consulta(mariposas_id):
    return jsonify({'message': 'Query updated successfully','id':mariposas_id})

def reset_complete_consulta(mariposas_id):
    return jsonify({'message': 'Query updated successfully','id':mariposas_id})