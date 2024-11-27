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

from API_TurboSMTP.models.subaccount_create_request import SubaccountCreateRequest

class TestSubaccountCreateRequest(unittest.TestCase):
    """SubaccountCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubaccountCreateRequest:
        """Test SubaccountCreateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubaccountCreateRequest`
        """
        model = SubaccountCreateRequest()
        if include_optional:
            return SubaccountCreateRequest(
                email = 'username@gmail.com',
                ip = '185.228.36.19',
                first_name = 'Andrea',
                last_name = 'Willems',
                address_1 = '51 Guild Street',
                address_2 = '1st Floor',
                city = 'London',
                company_name = 'Refreshing Soda Inc.',
                country = 'United Kingdom',
                region = 'West',
                zip_code = 'NW10 9NQ',
                phone_number = '5493513164544',
                policy_agree = True,
                site_url = 'https://www.refreshing-soda.com',
                password = 'LetmeIn123!',
                confirm_password = 'LetmeIn123!'
            )
        else:
            return SubaccountCreateRequest(
                email = 'username@gmail.com',
                ip = '185.228.36.19',
                first_name = 'Andrea',
                last_name = 'Willems',
                policy_agree = True,
                password = 'LetmeIn123!',
                confirm_password = 'LetmeIn123!',
        )
        """

    def testSubaccountCreateRequest(self):
        """Test SubaccountCreateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
