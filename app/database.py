import sqlite3
from flask import g

def get_db(app=None):
    """Получить соединение с базой данных."""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
        db.row_factory = sqlite3.Row
    return db


def close_db(e=None):
    """Закрыть соединение после запроса."""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def init_db(app):
    """Создаёт таблицу users и заполняет тестовыми данными."""
    with sqlite3.connect(app.config['DATABASE']) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        ''')

        cursor.executemany('''
            INSERT OR IGNORE INTO users (id, name, email)
            VALUES (?, ?, ?)
        ''', [
            (1, 'Иван', 'ivan@example.com'),
            (2, 'Мария', 'maria@example.com'),
            (3, 'Пётр', 'petr@example.com')
        ])
        conn.commit()
