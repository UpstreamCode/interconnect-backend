from uuid import uuid4
from datetime import datetime

from ..bootstrap import db
from .matchgroup_user import MatchgroupUser


class MatchGroup(db.Model):
    """A group of matched users"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pub_id = db.Column(db.Text, default=uuid4, unique=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    users = db.relationship(
        "User",
        secondary=MatchgroupUser,
        back_populates="matches")
