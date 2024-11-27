# ChangePasswordRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_password** | **str** | Current Password. | 
**password** | **str** | New Password to be used. | 
**confirm_password** | **str** | New Password to be used. | 

## Example

```python
from API_TurboSMTP.models.change_password_request_body import ChangePasswordRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ChangePasswordRequestBody from a JSON string
change_password_request_body_instance = ChangePasswordRequestBody.from_json(json)
# print the JSON string representation of the object
print ChangePasswordRequestBody.to_json()

# convert the object into a dict
change_password_request_body_dict = change_password_request_body_instance.to_dict()
# create an instance of ChangePasswordRequestBody from a dict
change_password_request_body_form_dict = change_password_request_body.from_dict(change_password_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


