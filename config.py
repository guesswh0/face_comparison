import os

BASE = os.path.abspath(os.path.dirname(__file__))


class Config:
    APP_NAME = 'face-comparison'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'
    PROJECT_ROOT = BASE

    # compare faces similarity threshold
    THRESHOLD = float(os.environ.get('THRESHOLD')) \
        if 'THRESHOLD' in os.environ else 0.85

    # FaceEngine models
    ENGINE_DETECTOR_NAME = os.environ.get('ENGINE_DETECTOR_NAME')
    ENGINE_EMBEDDER_NAME = os.environ.get('ENGINE_EMBEDDER_NAME')
    ENGINE_PREDICTOR_NAME = os.environ.get('ENGINE_PREDICTOR_NAME')


class DevConfig(Config):
    DEBUG = True
    TESTING = False


class TestConfig(Config):
    DEBUG = True
    TESTING = True


class ProdConfig(Config):
    DEBUG = False
    TESTING = False


config = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig,
    'default': DevConfig
}
