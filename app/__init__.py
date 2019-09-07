from face_engine import FaceEngine
from flask import Flask

from config import config

engine = FaceEngine()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # set FaceEngine detector model
    detector = app.config['ENGINE_DETECTOR_NAME']
    if detector:
        plugin = app.config['ENGINE_DETECTOR_PLUGIN']
        if plugin:
            engine.use_plugin(detector, plugin)
        else:
            engine.detector = detector
    # set FaceEngine embedder model
    embedder = app.config['ENGINE_EMBEDDER_NAME']
    if embedder:
        plugin = app.config['ENGINE_EMBEDDER_PLUGIN']
        if plugin:
            engine.use_plugin(embedder, plugin)
        else:
            engine.embedder = embedder

    from .api import api
    app.register_blueprint(api, url_prefix='/api')

    return app
