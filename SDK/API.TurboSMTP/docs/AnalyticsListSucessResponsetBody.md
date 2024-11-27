# AnalyticsListSucessResponsetBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**results** | [**List[AnalyticMailItem]**](AnalyticMailItem.md) |  | [optional] 

## Example

```python
from API_TurboSMTP.models.analytics_list_sucess_responset_body import AnalyticsListSucessResponsetBody

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsListSucessResponsetBody from a JSON string
analytics_list_sucess_responset_body_instance = AnalyticsListSucessResponsetBody.from_json(json)
# print the JSON string representation of the object
print AnalyticsListSucessResponsetBody.to_json()

# convert the object into a dict
analytics_list_sucess_responset_body_dict = analytics_list_sucess_responset_body_instance.to_dict()
# create an instance of AnalyticsListSucessResponsetBody from a dict
analytics_list_sucess_responset_body_form_dict = analytics_list_sucess_responset_body.from_dict(analytics_list_sucess_responset_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


