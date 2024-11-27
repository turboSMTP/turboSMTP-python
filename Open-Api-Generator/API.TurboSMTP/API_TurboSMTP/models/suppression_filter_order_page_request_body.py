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

from datetime import date
from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from API_TurboSMTP.models.list[suppression_source] import List[SuppressionSource]
from API_TurboSMTP.models.order_type import OrderType
from API_TurboSMTP.models.suppression_order_by import SuppressionOrderBy
from API_TurboSMTP.models.suppression_restriction import SuppressionRestriction
from typing import Optional, Set
from typing_extensions import Self

class SuppressionFilterOrderPageRequestBody(BaseModel):
    """
    SuppressionFilterOrderPageRequestBody
    """ # noqa: E501
    var_from: date = Field(description="Start date", alias="from")
    to: date = Field(description="End date")
    tz: Optional[StrictStr] = Field(default=None, description="Timezone Offset")
    filter: Optional[StrictStr] = Field(default=None, description="Query to search")
    filter_by: Optional[List[SuppressionSource]] = Field(default=None, description="Filter by")
    smart_search: Optional[StrictBool] = Field(default=False, description="Smart search")
    restrict: Optional[List[SuppressionRestriction]] = Field(default=None, description="xxxx")
    orderby: Optional[SuppressionOrderBy] = None
    ordertype: Optional[OrderType] = None
    page: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=1, description="Page number")
    limit: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=10, description="The numbers of rows per page to return")
    __properties: ClassVar[List[str]] = ["from", "to", "tz", "filter", "filter_by", "smart_search", "restrict", "orderby", "ordertype", "page", "limit"]

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
        """Create an instance of SuppressionFilterOrderPageRequestBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in restrict (list)
        _items = []
        if self.restrict:
            for _item in self.restrict:
                if _item:
                    _items.append(_item.to_dict())
            _dict['restrict'] = _items
        # set to None if smart_search (nullable) is None
        # and model_fields_set contains the field
        if self.smart_search is None and "smart_search" in self.model_fields_set:
            _dict['smart_search'] = None

        # set to None if page (nullable) is None
        # and model_fields_set contains the field
        if self.page is None and "page" in self.model_fields_set:
            _dict['page'] = None

        # set to None if limit (nullable) is None
        # and model_fields_set contains the field
        if self.limit is None and "limit" in self.model_fields_set:
            _dict['limit'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SuppressionFilterOrderPageRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "from": obj.get("from"),
            "to": obj.get("to"),
            "tz": obj.get("tz"),
            "filter": obj.get("filter"),
            "smart_search": obj.get("smart_search") if obj.get("smart_search") is not None else False,
            "restrict": [SuppressionRestriction.from_dict(_item) for _item in obj["restrict"]] if obj.get("restrict") is not None else None,
            "orderby": obj.get("orderby"),
            "ordertype": obj.get("ordertype"),
            "page": obj.get("page") if obj.get("page") is not None else 1,
            "limit": obj.get("limit") if obj.get("limit") is not None else 10
        })
        return _obj

