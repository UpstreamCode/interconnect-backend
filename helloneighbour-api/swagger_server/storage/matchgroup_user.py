from uuid import uuid4

from ..bootstrap import db


class MatchgroupUser(db.Model):
    """An join table between a user and a match"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    matchgroup_id = db.Column(db.Integer, db.ForeignKey('match_group.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

