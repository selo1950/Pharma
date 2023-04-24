from flask import Flask

from .routes import main

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Aguero16'
    
    app.register_blueprint(main)
    return(app)


