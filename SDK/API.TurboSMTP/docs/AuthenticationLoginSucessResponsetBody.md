# AuthenticationLoginSucessResponsetBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | **str** | API Key to be used in authorization header | [optional] 

## Example

```python
from API_TurboSMTP.models.authentication_login_sucess_responset_body import AuthenticationLoginSucessResponsetBody

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationLoginSucessResponsetBody from a JSON string
authentication_login_sucess_responset_body_instance = AuthenticationLoginSucessResponsetBody.from_json(json)
# print the JSON string representation of the object
print AuthenticationLoginSucessResponsetBody.to_json()

# convert the object into a dict
authentication_login_sucess_responset_body_dict = authentication_login_sucess_responset_body_instance.to_dict()
# create an instance of AuthenticationLoginSucessResponsetBody from a dict
authentication_login_sucess_responset_body_form_dict = authentication_login_sucess_responset_body.from_dict(authentication_login_sucess_responset_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


