# Authentication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authuser** | **str** | email of turboSMTP account | [optional] 
**authpass** | **str** | password of turboSMTP account | [optional] 

## Example

```python
from API_TurboSMTP.models.authentication import Authentication

# TODO update the JSON string below
json = "{}"
# create an instance of Authentication from a JSON string
authentication_instance = Authentication.from_json(json)
# print the JSON string representation of the object
print Authentication.to_json()

# convert the object into a dict
authentication_dict = authentication_instance.to_dict()
# create an instance of Authentication from a dict
authentication_form_dict = authentication.from_dict(authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


