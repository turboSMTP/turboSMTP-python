# SuppressionRestriction

Restriction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**by** | [**SuppressionRestrictBy**](SuppressionRestrictBy.md) |  | [optional] 
**operator** | [**SuppressionOperator**](SuppressionOperator.md) |  | [optional] 
**filter** | **str** |  | [optional] 
**smart_search** | **bool** | Smart search | [optional] [default to False]

## Example

```python
from API_TurboSMTP.models.suppression_restriction import SuppressionRestriction

# TODO update the JSON string below
json = "{}"
# create an instance of SuppressionRestriction from a JSON string
suppression_restriction_instance = SuppressionRestriction.from_json(json)
# print the JSON string representation of the object
print SuppressionRestriction.to_json()

# convert the object into a dict
suppression_restriction_dict = suppression_restriction_instance.to_dict()
# create an instance of SuppressionRestriction from a dict
suppression_restriction_form_dict = suppression_restriction.from_dict(suppression_restriction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


