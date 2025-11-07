from flask import Blueprint, jsonify, request, send_from_directory
from .models import User
from .extensions import db
import os

main = Blueprint('main', __name__)

# --- API: список всех пользователей ---
@main.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])

# --- API: получить пользователя по ID ---
@main.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "Пользователь не найден"}), 404
    return jsonify(user.to_dict())

# --- API: добавить пользователя ---
@main.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({"error": "Имя и email обязательны"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Пользователь с таким email уже существует"}), 409

    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict()), 201

# --- фронтенд ---
@main.route('/', defaults={'path': ''})
@main.route('/<path:path>')
def serve_frontend(path):
    static_folder = os.path.join(os.path.dirname(__file__), '..', 'static')
    if path != "" and os.path.exists(os.path.join(static_folder, path)):
        return send_from_directory(static_folder, path)
    return send_from_directory(static_folder, 'index.html')
