from flask import Blueprint, jsonify, abort, current_app
from .database import get_db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    """Главная страница"""
    return 'Добро пожаловать!'

@main.route('/users', methods=['GET'])
def get_users():
    """Возвращает список всех пользователей."""
    db = get_db(current_app)
    users = db.execute('SELECT * FROM users').fetchall()
    return jsonify([dict(u) for u in users])

@main.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Возвращает одного пользователя по ID."""
    db = get_db(current_app)
    user = db.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    if user is None:
        abort(404, description=f"Пользователь с id={user_id} не найден")
    return jsonify(dict(user))
