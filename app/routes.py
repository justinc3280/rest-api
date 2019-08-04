from app import app
from flask import jsonify

@app.route('/index')
def index():
    return jsonify({'Hello': 'World!', 'number': 5})

