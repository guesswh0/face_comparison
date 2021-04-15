import os


class Config:
    APP_NAME = 'face_comparison'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    # compare faces similarity threshold
    THRESHOLD = float(os.environ.get('THRESHOLD')) \
        if 'THRESHOLD' in os.environ else 0.85

    # FaceEngine models
    DETECTOR = os.environ.get('DETECTOR')
    EMBEDDER = os.environ.get('EMBEDDER')
    ESTIMATOR = os.environ.get('ESTIMATOR')
