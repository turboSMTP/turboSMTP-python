# AuthorizationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 

## Example

```python
from API_TurboSMTP.models.authorization_error import AuthorizationError

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationError from a JSON string
authorization_error_instance = AuthorizationError.from_json(json)
# print the JSON string representation of the object
print AuthorizationError.to_json()

# convert the object into a dict
authorization_error_dict = authorization_error_instance.to_dict()
# create an instance of AuthorizationError from a dict
authorization_error_form_dict = authorization_error.from_dict(authorization_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


