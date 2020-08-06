from face_engine import FaceEngine
from flask import Flask

from config import Config

engine = FaceEngine()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # set FaceEngine models
    engine.detector = app.config['ENGINE_DETECTOR_NAME']
    engine.embedder = app.config['ENGINE_EMBEDDER_NAME']
    engine.predictor = app.config['ENGINE_ESTIMATOR_NAME']

    from .api import api
    app.register_blueprint(api, url_prefix='/api')

    return app
