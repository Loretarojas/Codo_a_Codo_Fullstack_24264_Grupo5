from flask import Flask
from app.views import *

app = Flask(__name__)

# Rutas de Api-Rest 

app.route(' /', methods=['GET'])(index)

if __name__ == '__main__':
    app.run(debug=True)
