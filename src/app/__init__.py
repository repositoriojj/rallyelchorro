from flask import Flask

app = Flask(__name__)

# Configuración de la aplicación
app.config['SECRET_KEY'] = '0nlyC@nBe0ne'
app.template_folder = '../templates'
app = Flask(__name__, static_folder='../static')
# Registra las extensiones
# ...

from app.routes import *