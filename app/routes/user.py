from flask import Blueprint, request, jsonify, abort
from app.models import user as user_model

users_bp = Blueprint('users', __name__, url_prefix='/users')


@users_bp.route('', methods=['GET'])
def list_users():
    users = user_model.get_all_users()
    return jsonify(users), 200


@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    u = user_model.get_user(user_id)
    if u is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(u), 200


@users_bp.route('', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    if not username or not email or not password:
        return jsonify({'error': 'username, email and password required'}), 400
    try:
        created = user_model.create_user(username, email, password)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    return jsonify(created), 201


@users_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json() or {}
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    updated = user_model.update_user(user_id, username=username, email=email, password=password)
    if updated is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(updated), 200


@users_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    ok = user_model.delete_user(user_id)
    if not ok:
        return jsonify({'error': 'User not found'}), 404
    return '', 204
