from flask import Flask
from flask_cors import CORS

# Importar las vistas
from app.views import (
    index,
    get_pending_mariposas,
    get_completed_mariposas,
    get_mariposas,
    create_consulta,
    update_consulta,
    delete_mariposas,
    set_complete_mariposas,
    reset_complete_mariposas
)

# Importar la base de datos
from app.database import init_app, create_table_mariposas, insertar_mariposas

def create_app():
    # Crear la instancia de la aplicación Flask
    app = Flask(__name__)
    
    # Configuración de CORS
    CORS(app)

    # Inicializar la base de datos
    init_app(app)
    create_table_mariposas()

    # Rutas de Api-Rest
    app.route('/', methods=['GET'])(index)

    # CRUD
    app.route('/api/mariposas/pending/', methods=['GET'])(get_pending_mariposas)
    app.route('/api/mariposas/completed/', methods=['GET'])(get_completed_mariposas)
    app.route('/api/mariposas/fetch/<int:mariposas_id>/', methods=['GET'])(get_mariposas)
    app.route('/api/mariposas/create/', methods=['POST'])(create_consulta)
    app.route('/api/mariposas/update/<int:mariposas_id>/', methods=['PUT'])(update_consulta)
    app.route('/api/mariposas/complete/<int:mariposas_id>/', methods=['DELETE'])(delete_mariposas)
    app.route('/api/mariposas/complete/set/<int:mariposas_id>', methods=['PUT'])(set_complete_mariposas)
    app.route('/api/mariposas/complete/reset/<int:mariposas_id>', methods=['PUT'])(reset_complete_mariposas)

    # Insertar datos de ejemplo
    insertar_mariposas('Acrolophidae', 'Acrolophus', 'arcanella', 'USA', False, '2021-10-10')
    insertar_mariposas('Acrolophidae', 'Acrolophus', 'nr. cressoni', 'Mexico', False, '2021-10-10')

    return app

# Este bloque permite ejecutar la aplicación directamente usando `python -m app`
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
