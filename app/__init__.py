from flask import Flask
from .config import configure_app
from .logger import configure_logger
from .routes import init_routes

def create_app():
    app = Flask(__name__)
    configure_app(app)
    configure_logger(app)
    init_routes(app)
    return app
