from flask import Flask
from flask_cors import CORS

from app.views import *
from app.database import *


app = Flask(__name__)


# Rutas de la API-REST
app.route('/', methods=['GET'])(index)


app.route('/contacto/', methods=['GET'])(get_completed_contacto)

app.route('/contacto/fetch/<int:id>', methods=['GET'])(get_contacto)

app.route('/contacto/create/', methods=['POST'])(crear_contacto)
app.route('/contacto/update/<int:id>', methods=['PUT'])(actualizar_contacto)


app.route('/contacto/delete/<int:id>', methods=['DELETE'])(eliminar_contacto)
app.route('/contacto/complete/set/<int:id>', methods=['PUT'])(set_contacto)
app.route('/contacto/complete/reset/<int:id>', methods=['PUT'])(reset_contacto)

crear_contacto()

insertar_contacto('Laura', 'laura@gmail.com', 'consulta', 'abc', False, 'Argentina', 'Data')

# Conexión a BDD
init_app(app)

# Cors
CORS(app)


if __name__ == '__main__':
    app.run(debug=True)