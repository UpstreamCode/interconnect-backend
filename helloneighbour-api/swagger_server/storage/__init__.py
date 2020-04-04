from flask_sqlalchemy import SQLAlchemy

db = None


def init(app):
    db = SQLAlchemy(app)
    db.create_all()