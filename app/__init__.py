from flask import Flask

app = Flask(__name__)

# Configuración de la aplicación
app.config['SECRET_KEY'] = 'tu_clave_secreta'

# Registra las extensiones
# ...

from .routes import *