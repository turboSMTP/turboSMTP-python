# AuthenticationLoginRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The email of turboSMTP account | 
**password** | **str** | The password of turboSMTP account | 
**no_expire** | **bool** |  **false**:  authentication will expire after 2 hours.  **true**:  authentication will keep you signed in, and will never expire. (Use [/authentication/deauthorize](#/authentication/AuthenticationLogout) to logout and release your an API Key) | [optional] [default to False]

## Example

```python
from API_TurboSMTP.models.authentication_login_request_body import AuthenticationLoginRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationLoginRequestBody from a JSON string
authentication_login_request_body_instance = AuthenticationLoginRequestBody.from_json(json)
# print the JSON string representation of the object
print AuthenticationLoginRequestBody.to_json()

# convert the object into a dict
authentication_login_request_body_dict = authentication_login_request_body_instance.to_dict()
# create an instance of AuthenticationLoginRequestBody from a dict
authentication_login_request_body_form_dict = authentication_login_request_body.from_dict(authentication_login_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


