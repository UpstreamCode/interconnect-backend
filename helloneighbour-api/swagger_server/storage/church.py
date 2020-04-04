from uuid import uuid4

from ..bootstrap import db


class Church(db.Model):
    """ A church """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pub_id = db.Column(db.Text, default=uuid4, unique=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    address = db.Column(db.Text)
    website = db.Column(db.Text)
    email = db.Column(db.Text, unique=True, nullable=False)
    phone = db.Column(db.Text)
    group_size = db.Column(
        db.Integer,
        db.CheckConstraint('group_size in (2, 4, 6, 8, 10)', name='even_group')
    )
    same_gender = db.Column(db.Boolean, default=True)
    min_age = db.Column(
        db.Integer,
        db.CheckConstraint('min_age > 13', name="coppa_min_age")
    )
