from flask import Flask
from app.views import *
from app.database import *

app = Flask(__name__)

# Rutas de Api-Rest 

app.route('/', methods=['GET'])(index)

# CRUD
app.route('/api/mariposas/pending/', methods=['GET'])(get_pending_fluttersearch)

app.route('/api/mariposas/fetch/<int:mariposas_id>/', methods=['GET'])(get_mariposas)

app.route('/api/mariposas/create/', methods=['POST'])(create_consulta)

app.route('/api/mariposas/update/<int:mariposas_id>/', methods=['PUT'])(update_consulta)

app.route('/api/mariposas/complete/set/<int:mariposas_id>', methods=['PUT'])(set_complete_consulta)
app.route('/api/mariposas/complete/reset/<int:mariposas_id>', methods=['PUT'])(reset_complete_consulta)

# Conexión a BDD
init_app(app)

create_table_mariposas()

if __name__ == '__main__':
    app.run(debug=True)
