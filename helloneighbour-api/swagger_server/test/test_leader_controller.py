# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.church import Church  # noqa: E501
from swagger_server.models.church_in import ChurchIn  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.group import Group  # noqa: E501
from swagger_server.models.question import Question  # noqa: E501
from swagger_server.models.question_in import QuestionIn  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestLeaderController(BaseTestCase):
    """LeaderController integration test stubs"""

    def test_add_church(self):
        """Test case for add_church

        Add new church
        """
        body = ChurchIn()
        response = self.client.open(
            '/v0/church',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_question(self):
        """Test case for add_question

        Add question
        """
        body = QuestionIn()
        response = self.client.open(
            '/v0/church/{churchUuid}/question'.format(churchUuid='churchUuid_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_church(self):
        """Test case for delete_church

        Delete church
        """
        response = self.client.open(
            '/v0/church/{churchUuid}'.format(churchUuid='churchUuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_question(self):
        """Test case for delete_question

        Delete question
        """
        response = self.client.open(
            '/v0/church/{churchUuid}/question/{questionUuid}'.format(churchUuid='churchUuid_example', questionUuid='questionUuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_church(self):
        """Test case for edit_church

        Update church
        """
        body = ChurchIn()
        response = self.client.open(
            '/v0/church/{churchUuid}'.format(churchUuid='churchUuid_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_church(self):
        """Test case for get_church

        Retrieve church details
        """
        response = self.client.open(
            '/v0/church/{churchUuid}'.format(churchUuid='churchUuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_match_groups(self):
        """Test case for get_match_groups

        Retrieve list of all your church match groups
        """
        response = self.client.open(
            '/v0/church/{churchUuid}/matchgroups'.format(churchUuid='churchUuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_question(self):
        """Test case for get_question

        Retrieve question
        """
        response = self.client.open(
            '/v0/church/{churchUuid}/question/{questionUuid}'.format(churchUuid='churchUuid_example', questionUuid='questionUuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_questions(self):
        """Test case for get_questions

        Retrieve list of all your church questions
        """
        response = self.client.open(
            '/v0/church/{churchUuid}/questions'.format(churchUuid='churchUuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_users(self):
        """Test case for get_users

        Retrieve list of all your church members
        """
        response = self.client.open(
            '/v0/church/{churchUuid}/users'.format(churchUuid='churchUuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modify_question(self):
        """Test case for modify_question

        Update question
        """
        body = QuestionIn()
        response = self.client.open(
            '/v0/church/{churchUuid}/question/{questionUuid}'.format(churchUuid='churchUuid_example', questionUuid='questionUuid_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_send_invite(self):
        """Test case for send_invite

        Send invite
        """
        email = [List[str]()]
        response = self.client.open(
            '/v0/church/{churchUuid}/invite'.format(churchUuid='churchUuid_example'),
            method='POST',
            data=json.dumps(email),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
