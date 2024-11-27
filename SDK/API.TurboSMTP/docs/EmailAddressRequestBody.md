# EmailAddressRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | email address to validate | [optional] 

## Example

```python
from API_TurboSMTP.models.email_address_request_body import EmailAddressRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of EmailAddressRequestBody from a JSON string
email_address_request_body_instance = EmailAddressRequestBody.from_json(json)
# print the JSON string representation of the object
print EmailAddressRequestBody.to_json()

# convert the object into a dict
email_address_request_body_dict = email_address_request_body_instance.to_dict()
# create an instance of EmailAddressRequestBody from a dict
email_address_request_body_form_dict = email_address_request_body.from_dict(email_address_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


