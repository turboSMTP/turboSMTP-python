# Suppression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**sender** | **str** |  | [optional] 
**source** | [**SuppressionSource**](SuppressionSource.md) |  | [optional] 
**subject** | **str** |  | [optional] 
**recipient** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from API_TurboSMTP.models.suppression import Suppression

# TODO update the JSON string below
json = "{}"
# create an instance of Suppression from a JSON string
suppression_instance = Suppression.from_json(json)
# print the JSON string representation of the object
print Suppression.to_json()

# convert the object into a dict
suppression_dict = suppression_instance.to_dict()
# create an instance of Suppression from a dict
suppression_form_dict = suppression.from_dict(suppression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


