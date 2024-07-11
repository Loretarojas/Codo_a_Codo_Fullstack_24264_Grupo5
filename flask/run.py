
from flask import Flask
from flask_cors import CORS

from app.views import *
from app.database import *


app = Flask(__name__)


# Rutas de la API-REST
app.route('/', methods=['GET'])


app.route('/mariposa/', methods=['GET'])(get_completed_mariposa)

app.route('/mariposa/fetch/<int:id>', methods=['GET'])(get_mariposa)

app.route('/mariposa/', methods=['POST'])(crear_mariposa)
app.route('/mariposa/update/<int:id>', methods=['PUT'])(actualizar_mariposa)


app.route('/mariposa/delete/<int:id>', methods=['DELETE'])(eliminar_mariposa)
app.route('/mariposa/complete/set/<int:id>', methods=['PUT'])(set_mariposa)
app.route('/mariposa/complete/reset/<int:id>', methods=['PUT'])(reset_mariposa)

crear_mariposa()


# Conexión a BDD
init_app(app)

# Cors
CORS(app)


if __name__ == '__main__':
    app.run(debug=True)