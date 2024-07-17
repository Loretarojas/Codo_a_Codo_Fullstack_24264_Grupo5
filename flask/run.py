from flask import Flask
from flask_cors import CORS

from app.views import get_completed_mariposa, get_mariposa, crear_mariposa, actualizar_mariposa, eliminar_mariposa, index, set_mariposa, reset_mariposa
from app.database import init_app

app = Flask(__name__)

# Rutas de la API-REST
app.route('/', methods=['GET'])(index)
app.route('/mariposa/', methods=['GET'])(get_completed_mariposa)
app.route('/mariposa/fetch/<int:id>', methods=['GET'])(get_mariposa)
app.route('/mariposa/create/', methods=['POST'])(crear_mariposa)


# Conexión a BDD
init_app(app)

# Cors
CORS(app)


if __name__ == '__main__':
    app.run(debug=True)
