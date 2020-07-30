from face_engine import FaceEngine
from flask import Flask

from config import config

engine = FaceEngine()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # set FaceEngine models
    engine.detector = app.config['ENGINE_DETECTOR_NAME']
    engine.embedder = app.config['ENGINE_EMBEDDER_NAME']
    engine.predictor = app.config['ENGINE_ESTIMATOR_NAME']

    from .api import api
    app.register_blueprint(api, url_prefix='/api')

    return app
