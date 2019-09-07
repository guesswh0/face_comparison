from flask import jsonify


def bad_request(message):
    response = jsonify({'error': 'bad request', 'message': message})
    response.status_code = 400
    return response


def unprocessable(message):
    response = jsonify({'error': 'unprocessable entity', 'message': message})
    response.status_code = 422
    return response


def unsupported(message):
    response = jsonify({'error': 'unsupported media type', 'message': message})
    response.status_code = 415
    return response
