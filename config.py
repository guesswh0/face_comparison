import os


class Config:
    APP_NAME = 'face-comparison'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    # compare faces similarity threshold
    THRESHOLD = float(os.environ.get('THRESHOLD')) \
        if 'THRESHOLD' in os.environ else 0.85

    # FaceEngine models
    ENGINE_DETECTOR_NAME = os.environ.get('ENGINE_DETECTOR_NAME')
    ENGINE_EMBEDDER_NAME = os.environ.get('ENGINE_EMBEDDER_NAME')
    ENGINE_ESTIMATOR_NAME = os.environ.get('ENGINE_ESTIMATOR_NAME')
