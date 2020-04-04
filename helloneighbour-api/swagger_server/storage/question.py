from uuid import uuid4

from ..bootstrap import db


class Question(db.Model):
    """An icebreaker question"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pub_id = db.Column(db.Text, default=uuid4, unique=True)
    question = db.Column(db.Text)
    church_id = db.Column(db.Integer, db.ForeignKey('church.id'), nullable=False)

