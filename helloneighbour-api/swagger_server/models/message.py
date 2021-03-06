# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Message(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, group: str=None, user: str=None, sent: str=None, message: str=None, uuid: str=None):  # noqa: E501
        """Message - a model defined in Swagger

        :param group: The group of this Message.  # noqa: E501
        :type group: str
        :param user: The user of this Message.  # noqa: E501
        :type user: str
        :param sent: The sent of this Message.  # noqa: E501
        :type sent: str
        :param message: The message of this Message.  # noqa: E501
        :type message: str
        :param uuid: The uuid of this Message.  # noqa: E501
        :type uuid: str
        """
        self.swagger_types = {
            'group': str,
            'user': str,
            'sent': str,
            'message': str,
            'uuid': str
        }

        self.attribute_map = {
            'group': 'group',
            'user': 'user',
            'sent': 'sent',
            'message': 'message',
            'uuid': 'uuid'
        }

        self._group = group
        self._user = user
        self._sent = sent
        self._message = message
        self._uuid = uuid

    @classmethod
    def from_dict(cls, dikt) -> 'Message':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Message of this Message.  # noqa: E501
        :rtype: Message
        """
        return util.deserialize_model(dikt, cls)

    @property
    def group(self) -> str:
        """Gets the group of this Message.


        :return: The group of this Message.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group: str):
        """Sets the group of this Message.


        :param group: The group of this Message.
        :type group: str
        """

        self._group = group

    @property
    def user(self) -> str:
        """Gets the user of this Message.


        :return: The user of this Message.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user: str):
        """Sets the user of this Message.


        :param user: The user of this Message.
        :type user: str
        """

        self._user = user

    @property
    def sent(self) -> str:
        """Gets the sent of this Message.


        :return: The sent of this Message.
        :rtype: str
        """
        return self._sent

    @sent.setter
    def sent(self, sent: str):
        """Sets the sent of this Message.


        :param sent: The sent of this Message.
        :type sent: str
        """

        self._sent = sent

    @property
    def message(self) -> str:
        """Gets the message of this Message.


        :return: The message of this Message.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this Message.


        :param message: The message of this Message.
        :type message: str
        """

        self._message = message

    @property
    def uuid(self) -> str:
        """Gets the uuid of this Message.


        :return: The uuid of this Message.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid: str):
        """Sets the uuid of this Message.


        :param uuid: The uuid of this Message.
        :type uuid: str
        """

        self._uuid = uuid
