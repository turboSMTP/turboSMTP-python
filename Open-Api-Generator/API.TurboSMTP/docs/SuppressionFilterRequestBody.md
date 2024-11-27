# SuppressionFilterRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **date** | Start date | 
**to** | **date** | End date | 
**tz** | **str** | Timezone Offset | [optional] 
**filter** | **str** | Query to search | [optional] 
**filter_by** | [**List[SuppressionSource]**](SuppressionSource.md) | Filter by | [optional] 
**smart_search** | **bool** | Smart search | [optional] [default to False]
**restrict** | [**List[SuppressionRestriction]**](SuppressionRestriction.md) | xxxx | [optional] 

## Example

```python
from API_TurboSMTP.models.suppression_filter_request_body import SuppressionFilterRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of SuppressionFilterRequestBody from a JSON string
suppression_filter_request_body_instance = SuppressionFilterRequestBody.from_json(json)
# print the JSON string representation of the object
print SuppressionFilterRequestBody.to_json()

# convert the object into a dict
suppression_filter_request_body_dict = suppression_filter_request_body_instance.to_dict()
# create an instance of SuppressionFilterRequestBody from a dict
suppression_filter_request_body_form_dict = suppression_filter_request_body.from_dict(suppression_filter_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


