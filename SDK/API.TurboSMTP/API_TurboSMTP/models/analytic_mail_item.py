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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from API_TurboSMTP.models.analytic_mail_status import AnalyticMailStatus
from typing import Optional, Set
from typing_extensions import Self

class AnalyticMailItem(BaseModel):
    """
    Sent Email
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Email Id.")
    subject: Optional[StrictStr] = Field(default=None, description="Email Subject.")
    sender: Optional[StrictStr] = Field(default=None, description="Email Sender.")
    recipient: Optional[StrictStr] = Field(default=None, description="Email Recipient.")
    send_time: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Date Time email was sent.")
    status: Optional[AnalyticMailStatus] = None
    domain: Optional[StrictStr] = Field(default=None, description="The portion of the sender´s email address after the \"@\" symbol.")
    contact_domain: Optional[StrictStr] = Field(default=None, description="The portion of the recipient´s email address after the \"@\" symbol.")
    x_campaign_id: Optional[StrictStr] = Field(default=None, description="Value specified in the x_campaign_id custom header to track campaigns specific data.")
    error: Optional[StrictStr] = Field(default=None, description="Error returned when delivering the email message.")
    __properties: ClassVar[List[str]] = ["id", "subject", "sender", "recipient", "send_time", "status", "domain", "contact_domain", "x_campaign_id", "error"]

    @field_validator('send_time')
    def send_time_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", value):
            raise ValueError(r"must validate the regular expression /(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})/")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AnalyticMailItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AnalyticMailItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "subject": obj.get("subject"),
            "sender": obj.get("sender"),
            "recipient": obj.get("recipient"),
            "send_time": obj.get("send_time"),
            "status": obj.get("status"),
            "domain": obj.get("domain"),
            "contact_domain": obj.get("contact_domain"),
            "x_campaign_id": obj.get("x_campaign_id"),
            "error": obj.get("error")
        })
        return _obj


