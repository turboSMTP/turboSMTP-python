# State


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**iso_code** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from API_TurboSMTP.models.state import State

# TODO update the JSON string below
json = "{}"
# create an instance of State from a JSON string
state_instance = State.from_json(json)
# print the JSON string representation of the object
print State.to_json()

# convert the object into a dict
state_dict = state_instance.to_dict()
# create an instance of State from a dict
state_form_dict = state.from_dict(state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


