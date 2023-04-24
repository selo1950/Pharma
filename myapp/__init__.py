from flask import Flask

from .routes import main
from .excel_to_json import *

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Aguero16'
    
    app.register_blueprint(main)
    return(app)


