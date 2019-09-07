from face_engine import FaceError
from flask import Blueprint, request, jsonify, current_app
from skimage.io import imread

from . import engine
from .errors import bad_request, unsupported, unprocessable

api = Blueprint('api', __name__)


def allowed_files(filename):
    file_type = filename.rsplit('.', 1)[1].lower()
    return '.' in filename and \
           file_type in ['jpg', 'jpeg', 'png']


@api.route('/faces/compare', methods=['POST'])
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

    source_image = imread(source)
    target_image = imread(target)

    try:
        _, source_bb = engine.find_face(source_image)
    except FaceError as e:
        msg = e.args[0]
        msg += " on 'source' image"
        return unprocessable(msg)

    try:
        _, target_bbs = engine.find_faces(target_image)
    except FaceError as e:
        msg = e.args[0]
        msg += " on 'target' image"
        return unprocessable(msg)

    source_embedding = engine.compute_embeddings(source_image, [source_bb])
    target_embeddings = engine.compute_embeddings(target_image, target_bbs)
    _, score = engine._predictor.compare(source_embedding, target_embeddings)

    answer = dict()
    answer['FaceMatches'] = float(score) > current_app.config['THRESHOLD']
    answer['Similarity'] = score * 100
    return jsonify(answer), 200
