import connexion
import six

from swagger_server.models.church import Church  # noqa: E501
from swagger_server.models.church_in import ChurchIn  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.group import Group  # noqa: E501
from swagger_server.models.question import Question  # noqa: E501
from swagger_server.models.question_in import QuestionIn  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def add_church(body):  # noqa: E501
    """Add new church

    Add new church to the system to invite members to # noqa: E501

    :param body: Church details for new account
    :type body: dict | bytes

    :rtype: Church
    """
    if connexion.request.is_json:
        body = ChurchIn.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_question(churchUuid, body):  # noqa: E501
    """Add question

    Add a question to the system. # noqa: E501

    :param churchUuid: 
    :type churchUuid: 
    :param body: Question for the church
    :type body: dict | bytes

    :rtype: Question
    """
    if connexion.request.is_json:
        body = QuestionIn.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_church(churchUuid):  # noqa: E501
    """Delete church

    Delete a church from the system. # noqa: E501

    :param churchUuid: 
    :type churchUuid: 

    :rtype: None
    """
    return 'do some magic!'


def delete_question(churchUuid, questionUuid):  # noqa: E501
    """Delete question

    Delete a question from the system. # noqa: E501

    :param churchUuid: 
    :type churchUuid: 
    :param questionUuid: 
    :type questionUuid: 

    :rtype: None
    """
    return 'do some magic!'


def edit_church(churchUuid, body):  # noqa: E501
    """Update church

    Update church identified by church&#39;s UUID. All attributes can be edited. # noqa: E501

    :param churchUuid: 
    :type churchUuid: 
    :param body: New church details
    :type body: dict | bytes

    :rtype: ChurchIn
    """
    if connexion.request.is_json:
        body = ChurchIn.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_church(churchUuid):  # noqa: E501
    """Retrieve church details

    Retrieve church details. # noqa: E501

    :param churchUuid: 
    :type churchUuid: 

    :rtype: Church
    """
    return 'do some magic!'


def get_match_groups(churchUuid):  # noqa: E501
    """Retrieve list of all your church match groups

    Retrieve all match groups of a specific church. # noqa: E501

    :param churchUuid: 
    :type churchUuid: 

    :rtype: List[Group]
    """
    return 'do some magic!'


def get_question(churchUuid, questionUuid):  # noqa: E501
    """Retrieve question

    Retrieve a question for church for given UUIDs. # noqa: E501

    :param churchUuid: 
    :type churchUuid: 
    :param questionUuid: 
    :type questionUuid: 

    :rtype: Question
    """
    return 'do some magic!'


def get_questions(churchUuid):  # noqa: E501
    """Retrieve list of all your church questions

    Retrieve questions of a specific church. # noqa: E501

    :param churchUuid: 
    :type churchUuid: 

    :rtype: List[Question]
    """
    return 'do some magic!'


def get_users(churchUuid):  # noqa: E501
    """Retrieve list of all your church members

    Retrieve user details of all users of a specific church. # noqa: E501

    :param churchUuid: 
    :type churchUuid: 

    :rtype: List[User]
    """
    return 'do some magic!'


def modify_question(churchUuid, questionUuid, body):  # noqa: E501
    """Update question

    Update a question that&#39;s already in the system. # noqa: E501

    :param churchUuid: 
    :type churchUuid: 
    :param questionUuid: 
    :type questionUuid: 
    :param body: Question for the church
    :type body: dict | bytes

    :rtype: Question
    """
    if connexion.request.is_json:
        body = QuestionIn.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def send_invite(churchUuid, email):  # noqa: E501
    """Send invite

    Send an email invite to add new church members # noqa: E501

    :param churchUuid: 
    :type churchUuid: 
    :param email: 
    :type email: List[]

    :rtype: None
    """
    return 'do some magic!'
