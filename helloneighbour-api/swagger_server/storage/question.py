from .uuid_generator import uuid_str

from ..bootstrap import db


class Question(db.Model):
    """An icebreaker question"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pub_id = db.Column(db.Text, default=uuid_str, unique=True)
    question = db.Column(db.Text)
    church_id = db.Column(db.Integer, db.ForeignKey('church.id'), nullable=False)

