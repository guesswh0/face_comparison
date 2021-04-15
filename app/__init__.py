from face_engine import FaceEngine
from flask import Flask

from config import Config

engine = FaceEngine()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # set custom FaceEngine models
    engine.detector = app.config['DETECTOR']
    engine.embedder = app.config['EMBEDDER']
    engine.estimator = app.config['ESTIMATOR']

    from .api import api
    app.register_blueprint(api, url_prefix='/api')

    return app
