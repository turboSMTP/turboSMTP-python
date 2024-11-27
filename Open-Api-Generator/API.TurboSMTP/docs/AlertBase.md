# AlertBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**percentage** | **int** | Percentage of usage that will trigger the alert | [optional] 

## Example

```python
from API_TurboSMTP.models.alert_base import AlertBase

# TODO update the JSON string below
json = "{}"
# create an instance of AlertBase from a JSON string
alert_base_instance = AlertBase.from_json(json)
# print the JSON string representation of the object
print AlertBase.to_json()

# convert the object into a dict
alert_base_dict = alert_base_instance.to_dict()
# create an instance of AlertBase from a dict
alert_base_form_dict = alert_base.from_dict(alert_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


