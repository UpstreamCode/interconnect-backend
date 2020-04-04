from datetime import datetime
from uuid import uuid4

from ..bootstrap import db


class Bulletin(db.Model):
    """A bulletin to put on a board"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pub_id = db.Column(db.Text, default=uuid4().__str__, unique=True)
    match_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    sent = db.Column(db.DateTime, default=datetime.utcnow)
    message = db.Column(db.Text)
