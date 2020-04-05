import connexion
import six

from sqlalchemy import func, desc

from swagger_server.models.church_public import ChurchPublic  # noqa: E501
from swagger_server.models.contact_method import ContactMethod  # noqa: E501
from swagger_server.models.contact_method_in import ContactMethodIn  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.group import Group  # noqa: E501
from swagger_server.models.message import Message  # noqa: E501
from swagger_server.models.message_in import MessageIn  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_in import UserIn  # noqa: E501
from swagger_server import util
from swagger_server.controllers.common import IDENTITY_HEADER
from swagger_server.bootstrap import db
from swagger_server.storage.user import User as StorageUser
from swagger_server.storage.church import Church as StorageChurch
from swagger_server.storage.church import Church as StorageChurch


def add_contact_method(userUuid, body):  # noqa: E501
    """Add a contact method to a user profile

    Add a new contact method to an existing user profile. # noqa: E501

    :param userUuid: User&#39;s UUID
    :type userUuid: 
    :param body: Details of new contact method
    :type body: dict | bytes

    :rtype: ContactMethod
    """
    if connexion.request.is_json:
        body = ContactMethodIn.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_user(body):  # noqa: E501
    """Create new user account

    Create a new user to be authenticated via Firebase. Both church leaders and members need such an account. # noqa: E501

    :param body: User details for new account
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        body = UserIn.from_dict(connexion.request.get_json())  # noqa: E501
    
    firebase_id = connexion.request.headers.get(IDENTITY_HEADER)
    if not firebase_id:
        return ErrorResponse(code=401, message="Unauthenticated"), 401

    if not (body.first_name and body.email):
        return ErrorResponse(
            code=400,
            message="Missing first name or email from user"
        )

    newUserGroup = None
    last_group = db.session.query(StorageUser.group_num, func.count(StorageUser.group_num)).group_by(StorageUser.group_num).order_by(desc(StorageUser.group_num)).first()
    if last_group:
        if last_group[1] < 4:
            newUserGroup = last_group[0]
        else:
            newUserGroup = last_group[0] + 1
    else:
        newUserGroup = 1   

    user = StorageUser(
        first_name=body.first_name,
        last_name=body.last_name,
        email=body.email,
        description = body.description,
        church=1,
        role="member",
        group_num=newUserGroup,
        firebase_id=firebase_id
    )
    db.session.add(user)
    db.session.commit()
    
    ogChurch = db.session.query(StorageChurch).first()
    return User(
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        description=user.description,
        church=ogChurch.pub_id
    )


def delete_contact_method(userUuid, methodUuid):  # noqa: E501
    """Delete a contact method from a user profile

    Delete a contact method from a user profile. # noqa: E501

    :param userUuid: User&#39;s UUID
    :type userUuid: 
    :param methodUuid: Contact method&#39;s UUID
    :type methodUuid: 

    :rtype: None
    """
    return 'do some magic!'


def delete_user(userUuid):  # noqa: E501
    """Delete user

    Delete identified by user&#39;s UUID. # noqa: E501

    :param userUuid: 
    :type userUuid: 

    :rtype: None
    """
    return 'do some magic!'


def edit_user(userUuid, body):  # noqa: E501
    """Update user

    Update user identified by user&#39;s UUID. All attributes can be edited. # noqa: E501

    :param userUuid: 
    :type userUuid: 
    :param body: New user details
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        body = UserIn.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_church_public(userUuid, churchUuid):  # noqa: E501
    """Retrieve public church details

    Retrieve public church details. # noqa: E501

    :param userUuid: 
    :type userUuid: 
    :param churchUuid: 
    :type churchUuid: 

    :rtype: ChurchPublic
    """
    return 'do some magic!'


def get_match_group(churchUuid, userUuid):  # noqa: E501
    """Retrieve group

    Retrieve the group of the matched user. # noqa: E501

    :param churchUuid: 
    :type churchUuid: 
    :param userUuid: 
    :type userUuid: 

    :rtype: Group
    """
    firebase_id = connexion.request.headers.get(IDENTITY_HEADER)
    if not firebase_id:
        return ErrorResponse(code=401, message="Unauthenticated"), 401
    me = db.session.query(StorageUser).filter_by(firebase_id=firebase_id).first()
    if not me:
        return ErrorResponse(code=401, message="Unauthenticated"), 401
    group = []
    for u in db.session.query(StorageUser).filter_by(group_num=me.group_num).all():
         group.append(User(
             uuid=u.pub_id,
             first_name=u.first_name,
             last_name=u.last_name,
             email=u.email,
             description=u.description
         ))
    return group


def get_messages(userUuid, churchUuid, matchGroupUuid):  # noqa: E501
    """Retrieve all messages

    Retrieve messages posted on a group&#39;s bulletin. # noqa: E501

    :param userUuid: 
    :type userUuid: 
    :param churchUuid: 
    :type churchUuid: 
    :param matchGroupUuid: 
    :type matchGroupUuid: 

    :rtype: List[Message]
    """
    return 'do some magic!'


def get_user(userUuid):  # noqa: E501
    """Retrieve user details

    Retrieve user details. # noqa: E501

    :param userUuid: 
    :type userUuid: 

    :rtype: User
    """
    return 'do some magic!'


def send_message(userUuid, churchUuid, matchGroupUuid, body):  # noqa: E501
    """Send message

    Post a message to the group&#39;s bulletin. # noqa: E501

    :param userUuid: 
    :type userUuid: 
    :param churchUuid: 
    :type churchUuid: 
    :param matchGroupUuid: 
    :type matchGroupUuid: 
    :param body: Message to send to group
    :type body: dict | bytes

    :rtype: MessageIn
    """
    if connexion.request.is_json:
        body = MessageIn.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_contact_method(userUuid, methodUuid, body):  # noqa: E501
    """Update a contact method for a user

    Update a contact method for a user profile. # noqa: E501

    :param userUuid: User&#39;s UUID
    :type userUuid: 
    :param methodUuid: Contact method&#39;s UUID
    :type methodUuid: 
    :param body: New details of contact method
    :type body: dict | bytes

    :rtype: ContactMethod
    """
    if connexion.request.is_json:
        body = ContactMethodIn.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
