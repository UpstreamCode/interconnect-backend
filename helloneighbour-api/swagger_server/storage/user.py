import enum
from uuid import uuid4

from ..bootstrap import db
from .matchgroup_user import MatchgroupUser


class Gender(enum.Enum):
    male = "male"
    female = "female"


class Role(enum.Enum):
    leader = "leader"
    member = "member"


class User(db.Model):
    """ A user """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pub_id = db.Column(db.Text, default=uuid4, unique=True)
    fire_base_id = db.Column(db.Text)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=True)
    gender = db.Column(db.Enum(Gender))
    date_of_birth = db.Column(db.DateTime)
    email = db.Column(db.Text, unique=True, nullable=False)
    description = db.Column(db.Text)
    church_id = db.Column(
        db.Integer,
        db.ForeignKey('church.id'),
        nullable=False
    )
    role = db.Column(db.Enum(Role), nullable=False)

    matches = db.relationship(
        "MatchGroup",
        secondary=MatchgroupUser,
        back_populates="users")