import connexion
import six

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
    return 'do some magic!'


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
    return 'do some magic!'


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
