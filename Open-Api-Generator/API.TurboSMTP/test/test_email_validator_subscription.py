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

from API_TurboSMTP.models.email_validator_subscription import EmailValidatorSubscription

class TestEmailValidatorSubscription(unittest.TestCase):
    """EmailValidatorSubscription unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EmailValidatorSubscription:
        """Test EmailValidatorSubscription
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EmailValidatorSubscription`
        """
        model = EmailValidatorSubscription()
        if include_optional:
            return EmailValidatorSubscription(
                currency = '$',
                free_credits = 3000,
                free_credits_used = 200,
                last_used_period = '2022-11-20 00:00:00',
                latest_period_start_date = '2022-11-09 00:00:00',
                period_expiration_date = '2022-12-09 00:00:00',
                paid_credits = 437.456,
                remaining_free_credit = 2800
            )
        else:
            return EmailValidatorSubscription(
                currency = '$',
                free_credits = 3000,
                free_credits_used = 200,
                last_used_period = '2022-11-20 00:00:00',
                latest_period_start_date = '2022-11-09 00:00:00',
                period_expiration_date = '2022-12-09 00:00:00',
                paid_credits = 437.456,
        )
        """

    def testEmailValidatorSubscription(self):
        """Test EmailValidatorSubscription"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
