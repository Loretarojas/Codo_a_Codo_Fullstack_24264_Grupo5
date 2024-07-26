from flask import Flask
from flask_cors import CORS

from app.views import *
from app.database import *

app = Flask(__name__)



#CRUD
@app.route('/api/mariposa/', methods=['GET'])
def get_completed_mariposas():
    mariposas = Mariposa.get_all_mariposa()
    return jsonify([mariposa.serialize() for mariposa in mariposas])

@app.route('/api/mariposa/fetch/<int:id>', methods=['GET'])
def get_mariposa(id):
    mariposa = Mariposa.get_by_id(id)
    if mariposa:
        return jsonify(mariposa.serialize())
    else:
        return jsonify(message='Mariposa no encontrada'), 404

@app.route('/api/mariposa/create/', methods=['POST'])
def create_mariposa():
    data = request.json
    nuevo_mariposa = Mariposa(
        nombre=data['nombre'],
        especie=data['especie'],
        familia=data['familia'],
        nombreCientifico=data['nombreCientifico'],
        pais=data['pais']
  
    )
    nuevo_mariposa.save() 
    return jsonify(message='Mariposa creada'), 200



app.route('/api/mariposa/complete/set/<int:id>', methods=['PUT'])(set_mariposa)
app.route('/api/mariposa/complete/reset/<int:id>', methods=['PUT'])(reset_mariposa)

#crear_mariposa()

# Conexión a BDD
init_app(app)

# Cors
CORS(app)


if __name__ == '__main__':
    app.run(debug=True)
