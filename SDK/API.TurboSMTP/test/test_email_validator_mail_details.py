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

from API_TurboSMTP.models.email_validator_mail_details import EmailValidatorMailDetails

class TestEmailValidatorMailDetails(unittest.TestCase):
    """EmailValidatorMailDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EmailValidatorMailDetails:
        """Test EmailValidatorMailDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EmailValidatorMailDetails`
        """
        model = EmailValidatorMailDetails()
        if include_optional:
            return EmailValidatorMailDetails(
                email = 'username@gmail.com',
                status = 'valid',
                sub_status = '',
                free_email = True,
                domain = 'gmail.com',
                domain_age_days = 9964,
                smtp_provider = 'google',
                mx_found = True,
                mx_record = 'gmail-smtp-in.l.google.com',
                did_you_mean = 'the-user@gmail.com',
                account = 'username',
                firstname = 'Jhon',
                lastname = 'Doe',
                gender = 'female',
                country = '',
                region = '',
                city = '',
                zipcode = 56,
                processed_at = '2021-03-17 00:00:00'
            )
        else:
            return EmailValidatorMailDetails(
                email = 'username@gmail.com',
        )
        """

    def testEmailValidatorMailDetails(self):
        """Test EmailValidatorMailDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
