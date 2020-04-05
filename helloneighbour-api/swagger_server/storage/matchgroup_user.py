from ..bootstrap import db

matchgroup_user = db.Table(
    db.Column('match_group', db.Integer, db.ForeignKey('match_group.id'), nullable=False),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False),
)
