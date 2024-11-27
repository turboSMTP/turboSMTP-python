# AlertListSucessResponsetBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**results** | [**List[Alert]**](Alert.md) |  | [optional] 

## Example

```python
from API_TurboSMTP.models.alert_list_sucess_responset_body import AlertListSucessResponsetBody

# TODO update the JSON string below
json = "{}"
# create an instance of AlertListSucessResponsetBody from a JSON string
alert_list_sucess_responset_body_instance = AlertListSucessResponsetBody.from_json(json)
# print the JSON string representation of the object
print AlertListSucessResponsetBody.to_json()

# convert the object into a dict
alert_list_sucess_responset_body_dict = alert_list_sucess_responset_body_instance.to_dict()
# create an instance of AlertListSucessResponsetBody from a dict
alert_list_sucess_responset_body_form_dict = alert_list_sucess_responset_body.from_dict(alert_list_sucess_responset_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


