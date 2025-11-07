from flask import Blueprint, jsonify, send_from_directory
from .models import User
import os

main = Blueprint('main', __name__)

# API
@main.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])

@main.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "Пользователь не найден"}), 404
    return jsonify(user.to_dict())

# Фронтенд
@main.route('/', defaults={'path': ''})
@main.route('/<path:path>')
def serve_frontend(path):
    """Отдает статические файлы из static/"""
    static_folder = os.path.join(os.path.dirname(__file__), '..', 'static')
    if path != "" and os.path.exists(os.path.join(static_folder, path)):
        return send_from_directory(static_folder, path)
    return send_from_directory(static_folder, 'index.html')