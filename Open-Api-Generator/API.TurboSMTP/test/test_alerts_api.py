# coding: utf-8

"""
    TurboSMTP Public APIs

    This document describes all public turboSMTP **V2** API and offers endpoints Descriptions, Parameters, Requests, Responses and Samples of usage.  [Click here to view the previous version of turboSMTP Public API Version 1.0](https://www.serversmtp.com/turbo-api-1)   # Security For the most part (and where not otherwise explicit) turboSMTP’s API requires Authorization.   Authorization to access a user’s resource is granted to clients provided they set  authentication headers into their request, valued with the proper values issued by turboSMTP servers.  ## *  Authorization via ConsumerKey/ConsumerSecret  This type of authorization consists of a pair of headers, named consumerKey and consumerSecret that are created and granted to the end user to be used in a permanent way (unless they´re deleted of course). This kind of authentication is intended to provide access to endpoints features without the need of providing the user the account details (email address + password).  *consumerKey:* Consumer Key Granted.  *consumerSecret:* Consumer Secret Granted.  (Use [/consumerKeys/create](#/consumerkey/createConsumerKey) create a consumer key/secret pair).      ## *  Authorization via Authentication Key  The authentication key is user-based and it is issued by turboSMTP servers upon successful user’s email address + password challenge, performed by means of appropriate request.      *Authorization:* Authorization_Key  (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  # Data Interchange Format  For the most part (and where not otherwise explicit) turboSMTP’s API uses JSON as the data format of choice when it comes to request and response bodies.       

    The version of the OpenAPI document: 2.0.0-oas3
    Contact: api@turbo-smtp.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from API_TurboSMTP.api.alerts_api import AlertsApi


class TestAlertsApi(unittest.TestCase):
    """AlertsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AlertsApi()

    def tearDown(self) -> None:
        pass

    def test_create_alert(self) -> None:
        """Test case for create_alert

        Create new Alert Notification
        """
        pass

    def test_delete_alert(self) -> None:
        """Test case for delete_alert

        Delete Alert Notification
        """
        pass

    def test_get_alert(self) -> None:
        """Test case for get_alert

        Get Alert Notification
        """
        pass

    def test_get_alerts(self) -> None:
        """Test case for get_alerts

        Get Alerts Notifications Information
        """
        pass

    def test_update_alert(self) -> None:
        """Test case for update_alert

        Update Alert Notification
        """
        pass


if __name__ == '__main__':
    unittest.main()
