from .extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_dict(self):
        """Удобный метод для преобразования объекта в словарь JSON"""
        return {"id": self.id, "name": self.name, "email": self.email}
