# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class User(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, email: str=None, first_name: str=None, last_name: str=None, description: str=None, church: str=None, date_of_birth: date=None, uuid: str=None, contact: List[ContactMethod]=None):  # noqa: E501
        """User - a model defined in Swagger

        :param email: The email of this User.  # noqa: E501
        :type email: str
        :param first_name: The first_name of this User.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this User.  # noqa: E501
        :type last_name: str
        :param description: The description of this User.  # noqa: E501
        :type description: str
        :param church: The church of this User.  # noqa: E501
        :type church: str
        :param date_of_birth: The date_of_birth of this User.  # noqa: E501
        :type date_of_birth: date
        :param uuid: The uuid of this User.  # noqa: E501
        :type uuid: str
        :param contact: The contact of this User.  # noqa: E501
        :type contact: List[ContactMethod]
        """
        self.swagger_types = {
            'email': str,
            'first_name': str,
            'last_name': str,
            'description': str,
            'church': str,
            'date_of_birth': date,
            'uuid': str,
            'contact': List[ContactMethod]
        }

        self.attribute_map = {
            'email': 'email',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'description': 'description',
            'church': 'church',
            'date_of_birth': 'dateOfBirth',
            'uuid': 'uuid',
            'contact': 'contact'
        }

        self._email = email
        self._first_name = first_name
        self._last_name = last_name
        self._description = description
        self._church = church
        self._date_of_birth = date_of_birth
        self._uuid = uuid
        self._contact = contact

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.  # noqa: E501
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def email(self) -> str:
        """Gets the email of this User.


        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this User.


        :param email: The email of this User.
        :type email: str
        """

        self._email = email

    @property
    def first_name(self) -> str:
        """Gets the first_name of this User.


        :return: The first_name of this User.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first_name of this User.


        :param first_name: The first_name of this User.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """Gets the last_name of this User.


        :return: The last_name of this User.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this User.


        :param last_name: The last_name of this User.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def description(self) -> str:
        """Gets the description of this User.


        :return: The description of this User.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this User.


        :param description: The description of this User.
        :type description: str
        """

        self._description = description

    @property
    def church(self) -> str:
        """Gets the church of this User.


        :return: The church of this User.
        :rtype: str
        """
        return self._church

    @church.setter
    def church(self, church: str):
        """Sets the church of this User.


        :param church: The church of this User.
        :type church: str
        """

        self._church = church

    @property
    def date_of_birth(self) -> date:
        """Gets the date_of_birth of this User.


        :return: The date_of_birth of this User.
        :rtype: date
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth: date):
        """Sets the date_of_birth of this User.


        :param date_of_birth: The date_of_birth of this User.
        :type date_of_birth: date
        """

        self._date_of_birth = date_of_birth

    @property
    def uuid(self) -> str:
        """Gets the uuid of this User.


        :return: The uuid of this User.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid: str):
        """Sets the uuid of this User.


        :param uuid: The uuid of this User.
        :type uuid: str
        """

        self._uuid = uuid

    @property
    def contact(self) -> List[ContactMethod]:
        """Gets the contact of this User.


        :return: The contact of this User.
        :rtype: List[ContactMethod]
        """
        return self._contact

    @contact.setter
    def contact(self, contact: List[ContactMethod]):
        """Sets the contact of this User.


        :param contact: The contact of this User.
        :type contact: List[ContactMethod]
        """

        self._contact = contact
