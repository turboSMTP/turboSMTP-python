# coding: utf-8

"""
    TurboSMTP Public APIs

    This document describes all public turboSMTP **V2** API and offers endpoints Descriptions, Parameters, Requests, Responses and Samples of usage.  [Click here to view the previous version of turboSMTP Public API Version 1.0](https://www.serversmtp.com/turbo-api-1)   # Security For the most part (and where not otherwise explicit) turboSMTP’s API requires Authorization.   Authorization to access a user’s resource is granted to clients provided they set  authentication headers into their request, valued with the proper values issued by turboSMTP servers.  ## *  Authorization via ConsumerKey/ConsumerSecret  This type of authorization consists of a pair of headers, named consumerKey and consumerSecret that are created and granted to the end user to be used in a permanent way (unless they´re deleted of course). This kind of authentication is intended to provide access to endpoints features without the need of providing the user the account details (email address + password).  *consumerKey:* Consumer Key Granted.  *consumerSecret:* Consumer Secret Granted.  (Use [/consumerKeys/create](#/consumerkey/createConsumerKey) create a consumer key/secret pair).      ## *  Authorization via Authentication Key  The authentication key is user-based and it is issued by turboSMTP servers upon successful user’s email address + password challenge, performed by means of appropriate request.      *Authorization:* Authorization_Key  (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  # Data Interchange Format  For the most part (and where not otherwise explicit) turboSMTP’s API uses JSON as the data format of choice when it comes to request and response bodies.       

    The version of the OpenAPI document: 2.0.0-oas3
    Contact: api@turbo-smtp.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AnalyticMailStatus(str, Enum):
    """
    Send Mail Status:  NEW: email has been queued for delivery DEFER: email is in the queue for delivery SUCCESS: email has been delivered. OPEN: email has been opened. CLICK: email has been clicked. REPORT: email has been reported as spam. FAIL: email has bounced. SYSFAIL: email was dropped. UNSUB: email is unsubscribed.  Notice that emails that fall into the above statuses can be grouped, ie Turbo-Smtp uses the following groups:    'Clicks' = 'CLICK',   'Unsubscribes' = 'UNSUB',   'Spam' = 'REPORT',   'Drop' = 'SYSFAIL',   'Queued' = 'NEW' or 'DEFER',   'Opens'= 'OPEN' or 'CLICK' or 'UNSUB' or 'REPORT',   'Delivered'= 'SUCCESS'  or 'OPEN' or 'CLICK' or 'UNSUB' or 'REPORT',   'Bounce': 'FAIL'. 
    """

    """
    allowed enum values
    """
    NEW = 'NEW'
    DEFER = 'DEFER'
    SUCCESS = 'SUCCESS'
    OPEN = 'OPEN'
    CLICK = 'CLICK'
    REPORT = 'REPORT'
    FAIL = 'FAIL'
    SYSFAIL = 'SYSFAIL'
    UNSUB = 'UNSUB'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AnalyticMailStatus from a JSON string"""
        return cls(json.loads(json_str))


