from .uuid_generator import uuid_str

from ..bootstrap import db


class ContactMethod(db.Model):
    """A means of contacting a user"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pub_id = db.Column(db.Text, default=uuid_str, unique=True)
    label = db.Column(db.Text)
    contact_details = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

