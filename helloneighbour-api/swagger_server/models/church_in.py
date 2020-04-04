# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ChurchIn(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, description: str=None, address: str=None, website: str=None, email: str=None, phone: str=None, main_contact: str=None, group_size: int=None, same_gender: bool=None, min_age: int=None):  # noqa: E501
        """ChurchIn - a model defined in Swagger

        :param name: The name of this ChurchIn.  # noqa: E501
        :type name: str
        :param description: The description of this ChurchIn.  # noqa: E501
        :type description: str
        :param address: The address of this ChurchIn.  # noqa: E501
        :type address: str
        :param website: The website of this ChurchIn.  # noqa: E501
        :type website: str
        :param email: The email of this ChurchIn.  # noqa: E501
        :type email: str
        :param phone: The phone of this ChurchIn.  # noqa: E501
        :type phone: str
        :param main_contact: The main_contact of this ChurchIn.  # noqa: E501
        :type main_contact: str
        :param group_size: The group_size of this ChurchIn.  # noqa: E501
        :type group_size: int
        :param same_gender: The same_gender of this ChurchIn.  # noqa: E501
        :type same_gender: bool
        :param min_age: The min_age of this ChurchIn.  # noqa: E501
        :type min_age: int
        """
        self.swagger_types = {
            'name': str,
            'description': str,
            'address': str,
            'website': str,
            'email': str,
            'phone': str,
            'main_contact': str,
            'group_size': int,
            'same_gender': bool,
            'min_age': int
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'address': 'address',
            'website': 'website',
            'email': 'email',
            'phone': 'phone',
            'main_contact': 'main_contact',
            'group_size': 'group_size',
            'same_gender': 'same_gender',
            'min_age': 'min_age'
        }

        self._name = name
        self._description = description
        self._address = address
        self._website = website
        self._email = email
        self._phone = phone
        self._main_contact = main_contact
        self._group_size = group_size
        self._same_gender = same_gender
        self._min_age = min_age

    @classmethod
    def from_dict(cls, dikt) -> 'ChurchIn':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ChurchIn of this ChurchIn.  # noqa: E501
        :rtype: ChurchIn
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this ChurchIn.


        :return: The name of this ChurchIn.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ChurchIn.


        :param name: The name of this ChurchIn.
        :type name: str
        """

        self._name = name

    @property
    def description(self) -> str:
        """Gets the description of this ChurchIn.


        :return: The description of this ChurchIn.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this ChurchIn.


        :param description: The description of this ChurchIn.
        :type description: str
        """

        self._description = description

    @property
    def address(self) -> str:
        """Gets the address of this ChurchIn.


        :return: The address of this ChurchIn.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str):
        """Sets the address of this ChurchIn.


        :param address: The address of this ChurchIn.
        :type address: str
        """

        self._address = address

    @property
    def website(self) -> str:
        """Gets the website of this ChurchIn.


        :return: The website of this ChurchIn.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website: str):
        """Sets the website of this ChurchIn.


        :param website: The website of this ChurchIn.
        :type website: str
        """

        self._website = website

    @property
    def email(self) -> str:
        """Gets the email of this ChurchIn.


        :return: The email of this ChurchIn.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this ChurchIn.


        :param email: The email of this ChurchIn.
        :type email: str
        """

        self._email = email

    @property
    def phone(self) -> str:
        """Gets the phone of this ChurchIn.


        :return: The phone of this ChurchIn.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone: str):
        """Sets the phone of this ChurchIn.


        :param phone: The phone of this ChurchIn.
        :type phone: str
        """

        self._phone = phone

    @property
    def main_contact(self) -> str:
        """Gets the main_contact of this ChurchIn.


        :return: The main_contact of this ChurchIn.
        :rtype: str
        """
        return self._main_contact

    @main_contact.setter
    def main_contact(self, main_contact: str):
        """Sets the main_contact of this ChurchIn.


        :param main_contact: The main_contact of this ChurchIn.
        :type main_contact: str
        """

        self._main_contact = main_contact

    @property
    def group_size(self) -> int:
        """Gets the group_size of this ChurchIn.


        :return: The group_size of this ChurchIn.
        :rtype: int
        """
        return self._group_size

    @group_size.setter
    def group_size(self, group_size: int):
        """Sets the group_size of this ChurchIn.


        :param group_size: The group_size of this ChurchIn.
        :type group_size: int
        """
        if group_size is not None and group_size > 10:  # noqa: E501
            raise ValueError("Invalid value for `group_size`, must be a value less than or equal to `10`")  # noqa: E501
        if group_size is not None and group_size < 2:  # noqa: E501
            raise ValueError("Invalid value for `group_size`, must be a value greater than or equal to `2`")  # noqa: E501

        self._group_size = group_size

    @property
    def same_gender(self) -> bool:
        """Gets the same_gender of this ChurchIn.


        :return: The same_gender of this ChurchIn.
        :rtype: bool
        """
        return self._same_gender

    @same_gender.setter
    def same_gender(self, same_gender: bool):
        """Sets the same_gender of this ChurchIn.


        :param same_gender: The same_gender of this ChurchIn.
        :type same_gender: bool
        """

        self._same_gender = same_gender

    @property
    def min_age(self) -> int:
        """Gets the min_age of this ChurchIn.


        :return: The min_age of this ChurchIn.
        :rtype: int
        """
        return self._min_age

    @min_age.setter
    def min_age(self, min_age: int):
        """Sets the min_age of this ChurchIn.


        :param min_age: The min_age of this ChurchIn.
        :type min_age: int
        """

        self._min_age = min_age