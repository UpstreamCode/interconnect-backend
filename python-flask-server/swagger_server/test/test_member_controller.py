# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.church_public import ChurchPublic  # noqa: E501
from swagger_server.models.contact_method import ContactMethod  # noqa: E501
from swagger_server.models.contact_method_in import ContactMethodIn  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.group import Group  # noqa: E501
from swagger_server.models.message import Message  # noqa: E501
from swagger_server.models.message_in import MessageIn  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_in import UserIn  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMemberController(BaseTestCase):
    """MemberController integration test stubs"""

    def test_add_contact_method(self):
        """Test case for add_contact_method

        Add a contact method to a user profile
        """
        body = ContactMethodIn()
        response = self.client.open(
            '/v0/user/{userUuid}/contactmethod'.format(userUuid='userUuid_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_user(self):
        """Test case for create_user

        Create new user account
        """
        body = UserIn()
        response = self.client.open(
            '/v0/user',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_contact_method(self):
        """Test case for delete_contact_method

        Delete a contact method from a user profile
        """
        response = self.client.open(
            '/v0/user/{userUuid}/contactmethod/{methodUuid}'.format(userUuid='userUuid_example', methodUuid='methodUuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_user(self):
        """Test case for delete_user

        Delete user
        """
        response = self.client.open(
            '/v0/user/{userUuid}'.format(userUuid='userUuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_user(self):
        """Test case for edit_user

        Update user
        """
        body = UserIn()
        response = self.client.open(
            '/v0/user/{userUuid}'.format(userUuid='userUuid_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_church_public(self):
        """Test case for get_church_public

        Retrieve public church details
        """
        response = self.client.open(
            '/v0/user/{userUuid}/church/{churchUuid}'.format(userUuid='userUuid_example', churchUuid='churchUuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_match_group(self):
        """Test case for get_match_group

        Retrieve group
        """
        response = self.client.open(
            '/v0/user/{userUuid}/church/{churchUuid}/matchgroup'.format(churchUuid='churchUuid_example', userUuid='userUuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_messages(self):
        """Test case for get_messages

        Retrieve all messages
        """
        response = self.client.open(
            '/v0/user/{userUuid}/church/{churchUuid}/matchgroup/{matchGroupUuid}/bulletin'.format(userUuid='userUuid_example', churchUuid='churchUuid_example', matchGroupUuid='matchGroupUuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user(self):
        """Test case for get_user

        Retrieve user details
        """
        response = self.client.open(
            '/v0/user/{userUuid}'.format(userUuid='userUuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_send_message(self):
        """Test case for send_message

        Send message
        """
        body = MessageIn()
        response = self.client.open(
            '/v0/user/{userUuid}/church/{churchUuid}/matchgroup/{matchGroupUuid}/bulletin'.format(userUuid='userUuid_example', churchUuid='churchUuid_example', matchGroupUuid='matchGroupUuid_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_contact_method(self):
        """Test case for update_contact_method

        Update a contact method for a user
        """
        body = ContactMethodIn()
        response = self.client.open(
            '/v0/user/{userUuid}/contactmethod/{methodUuid}'.format(userUuid='userUuid_example', methodUuid='methodUuid_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
