from face_engine.exceptions import FaceNotFoundError
from flask import Blueprint, request, jsonify, current_app

from . import engine
from .errors import bad_request, unsupported, unprocessable

api = Blueprint('api', __name__)


def allowed_files(filename):
    file_type = filename.rsplit('.', 1)[1].lower()
    return '.' in filename and \
           file_type in ['jpg', 'jpeg', 'png']


@api.route('/compare_faces', methods=['POST'])
def compare_faces():
    if 'source' not in request.files:
        return bad_request('no source file')

    if 'target' not in request.files:
        return bad_request('no target file')

    source = request.files.get('source')
    if source is None or not allowed_files(source.filename):
        return unsupported("'source' image file type is not supported")

    target = request.files.get('target')
    if target is None or not allowed_files(target.filename):
        return unsupported("'target' image file type is not supported")

    try:
        score = engine.compare_faces(source, target)[0]
    except FaceNotFoundError:
        return unprocessable('Face not found error')

    answer = dict()
    answer['FaceMatches'] = float(score) > current_app.config['THRESHOLD']
    answer['Similarity'] = score * 100
    return jsonify(answer), 200
