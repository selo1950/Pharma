from flask import Flask
from .routes import app
from .samolijecenje import medicine_clean
from .forms import *

def create_app():

    return app