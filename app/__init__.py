from flask import Flask
from .extensions import db
from .errors import register_error_handlers

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Локальные импорты внутри функции
    with app.app_context():
        from .models import User
        from .routes import main

        db.create_all()

        # Добавляем тестовых пользователей, если таблица пуста
        if User.query.count() == 0:
            test_users = [
                User(name="Иван", email="ivan@example.com"),
                User(name="Мария", email="maria@example.com"),
                User(name="Пётр", email="petr@example.com")
            ]
            db.session.add_all(test_users)
            db.session.commit()

        app.register_blueprint(main)
        register_error_handlers(app)

    return app
