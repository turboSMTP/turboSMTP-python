# SendSecretTokenResetPasswordRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | turboSMTP account email address. | 

## Example

```python
from API_TurboSMTP.models.send_secret_token_reset_password_request_body import SendSecretTokenResetPasswordRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of SendSecretTokenResetPasswordRequestBody from a JSON string
send_secret_token_reset_password_request_body_instance = SendSecretTokenResetPasswordRequestBody.from_json(json)
# print the JSON string representation of the object
print SendSecretTokenResetPasswordRequestBody.to_json()

# convert the object into a dict
send_secret_token_reset_password_request_body_dict = send_secret_token_reset_password_request_body_instance.to_dict()
# create an instance of SendSecretTokenResetPasswordRequestBody from a dict
send_secret_token_reset_password_request_body_form_dict = send_secret_token_reset_password_request_body.from_dict(send_secret_token_reset_password_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


