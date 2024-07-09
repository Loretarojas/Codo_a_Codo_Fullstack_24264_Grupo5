from flask import Flask
from app.views import *
from app.database import *
from flask_cors import CORS

app = Flask(__name__)

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

create_table_mariposas()

insertar_mariposas ('Acrolophidae', 'Acrolophus', 'arcanella', 'USA', False, '2021-10-10')   
insertar_mariposas('Acrolophidae', 'Acrolophus', 'nr. cressoni', 'Mexico', False, '2021-10-10')

   



# Conexión a BDD
init_app(app)

#CORS
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)
