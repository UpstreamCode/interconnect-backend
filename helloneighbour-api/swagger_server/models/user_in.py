# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class UserIn(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, email: str=None, first_name: str=None, last_name: str=None, description: str=None, church: str=None, date_of_birth: date=None):  # noqa: E501
        """UserIn - a model defined in Swagger

        :param email: The email of this UserIn.  # noqa: E501
        :type email: str
        :param first_name: The first_name of this UserIn.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this UserIn.  # noqa: E501
        :type last_name: str
        :param description: The description of this UserIn.  # noqa: E501
        :type description: str
        :param church: The church of this UserIn.  # noqa: E501
        :type church: str
        :param date_of_birth: The date_of_birth of this UserIn.  # noqa: E501
        :type date_of_birth: date
        """
        self.swagger_types = {
            'email': str,
            'first_name': str,
            'last_name': str,
            'description': str,
            'church': str,
            'date_of_birth': date
        }

        self.attribute_map = {
            'email': 'email',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'description': 'description',
            'church': 'church',
            'date_of_birth': 'dateOfBirth'
        }

        self._email = email
        self._first_name = first_name
        self._last_name = last_name
        self._description = description
        self._church = church
        self._date_of_birth = date_of_birth

    @classmethod
    def from_dict(cls, dikt) -> 'UserIn':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UserIn of this UserIn.  # noqa: E501
        :rtype: UserIn
        """
        return util.deserialize_model(dikt, cls)

    @property
    def email(self) -> str:
        """Gets the email of this UserIn.


        :return: The email of this UserIn.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this UserIn.


        :param email: The email of this UserIn.
        :type email: str
        """

        self._email = email

    @property
    def first_name(self) -> str:
        """Gets the first_name of this UserIn.


        :return: The first_name of this UserIn.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first_name of this UserIn.


        :param first_name: The first_name of this UserIn.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """Gets the last_name of this UserIn.


        :return: The last_name of this UserIn.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this UserIn.


        :param last_name: The last_name of this UserIn.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def description(self) -> str:
        """Gets the description of this UserIn.


        :return: The description of this UserIn.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this UserIn.


        :param description: The description of this UserIn.
        :type description: str
        """

        self._description = description

    @property
    def church(self) -> str:
        """Gets the church of this UserIn.


        :return: The church of this UserIn.
        :rtype: str
        """
        return self._church

    @church.setter
    def church(self, church: str):
        """Sets the church of this UserIn.


        :param church: The church of this UserIn.
        :type church: str
        """

        self._church = church

    @property
    def date_of_birth(self) -> date:
        """Gets the date_of_birth of this UserIn.


        :return: The date_of_birth of this UserIn.
        :rtype: date
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth: date):
        """Sets the date_of_birth of this UserIn.


        :param date_of_birth: The date_of_birth of this UserIn.
        :type date_of_birth: date
        """

        self._date_of_birth = date_of_birth