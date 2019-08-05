from app import app
from flask import jsonify, request
from werkzeug.http import HTTP_STATUS_CODES

data = {'hello': 'WORLD!'}

# @app.route('/index')
# def index():
#     return jsonify({'Hello': 'World!', 'number': 5})



@app.route('/<string:key>')
def get_key(key):
    if key in data:
        return jsonify({key: data[key]})
    else:
        return error_response(404, 'key not found')


@app.route('/set', methods=['POST'])
def set_value():
    request_data = request.get_json()
    if not request_data:
        return error_response(400, 'please include data')
    elif len(request_data) > 1:
        return error_response(400, 'only 1 value please')
    else:
        for key, value in request_data.items():
            if key in data:
                data[key] = value
                response = jsonify({key: value})
                response.status_code = 200
                return response
            else:
                data[key] = value
                response = jsonify({key: value})
                response.status_code = 201
                return response


def error_response(error_code, message=None):
    payload = { 'error': HTTP_STATUS_CODES.get(error_code, "Unknown Error")}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = error_code
    return response


@app.errorhandler(404)
def error_404(error):
    return error_response(404, 'URL not found')
