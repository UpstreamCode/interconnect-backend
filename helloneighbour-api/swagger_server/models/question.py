# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Question(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, question: str=None, church: str=None, uuid: str=None):  # noqa: E501
        """Question - a model defined in Swagger

        :param question: The question of this Question.  # noqa: E501
        :type question: str
        :param church: The church of this Question.  # noqa: E501
        :type church: str
        :param uuid: The uuid of this Question.  # noqa: E501
        :type uuid: str
        """
        self.swagger_types = {
            'question': str,
            'church': str,
            'uuid': str
        }

        self.attribute_map = {
            'question': 'question',
            'church': 'church',
            'uuid': 'uuid'
        }

        self._question = question
        self._church = church
        self._uuid = uuid

    @classmethod
    def from_dict(cls, dikt) -> 'Question':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Question of this Question.  # noqa: E501
        :rtype: Question
        """
        return util.deserialize_model(dikt, cls)

    @property
    def question(self) -> str:
        """Gets the question of this Question.


        :return: The question of this Question.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question: str):
        """Sets the question of this Question.


        :param question: The question of this Question.
        :type question: str
        """

        self._question = question

    @property
    def church(self) -> str:
        """Gets the church of this Question.


        :return: The church of this Question.
        :rtype: str
        """
        return self._church

    @church.setter
    def church(self, church: str):
        """Sets the church of this Question.


        :param church: The church of this Question.
        :type church: str
        """

        self._church = church

    @property
    def uuid(self) -> str:
        """Gets the uuid of this Question.


        :return: The uuid of this Question.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid: str):
        """Sets the uuid of this Question.


        :param uuid: The uuid of this Question.
        :type uuid: str
        """

        self._uuid = uuid