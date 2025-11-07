from flask import Flask
from .database import init_db
from .routes import main
from .errors import register_error_handlers

def create_app():
    app = Flask(__name__)
    app.config['DATABASE'] = 'users.db'

    # Инициализация базы данных
    init_db(app)

    # Регистрация blueprint и ошибок
    app.register_blueprint(main)
    register_error_handlers(app)

    return app
