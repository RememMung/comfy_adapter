from flask import Blueprint, jsonify

bp = Blueprint('my_routes', __name__)

@bp.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})