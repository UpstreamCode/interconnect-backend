from .uuid_generator import uuid_str
from datetime import datetime

from ..bootstrap import db
from .user import User
from .matchgroup_user import matchgroup_user


class MatchGroup(db.Model):
    """A group of matched users"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pub_id = db.Column(db.Text, default=uuid_str, unique=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    question = db.Column(
        db.Integer,
        db.ForeignKey('question.id'),
        nullable=False
    )

    users = db.relationship(
        User,
        secondary=matchgroup_user,
        backref="matches"
    )
