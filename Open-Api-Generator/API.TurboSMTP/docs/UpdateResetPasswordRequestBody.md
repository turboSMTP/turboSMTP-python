# UpdateResetPasswordRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | New Password to be used. | 
**confirm_password** | **str** | New Password to be used. | 
**token** | **str** | Reset Password Token | 

## Example

```python
from API_TurboSMTP.models.update_reset_password_request_body import UpdateResetPasswordRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateResetPasswordRequestBody from a JSON string
update_reset_password_request_body_instance = UpdateResetPasswordRequestBody.from_json(json)
# print the JSON string representation of the object
print UpdateResetPasswordRequestBody.to_json()

# convert the object into a dict
update_reset_password_request_body_dict = update_reset_password_request_body_instance.to_dict()
# create an instance of UpdateResetPasswordRequestBody from a dict
update_reset_password_request_body_form_dict = update_reset_password_request_body.from_dict(update_reset_password_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


