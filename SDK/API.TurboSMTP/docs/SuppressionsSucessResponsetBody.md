# SuppressionsSucessResponsetBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**results** | [**List[Suppression]**](Suppression.md) |  | [optional] 

## Example

```python
from API_TurboSMTP.models.suppressions_sucess_responset_body import SuppressionsSucessResponsetBody

# TODO update the JSON string below
json = "{}"
# create an instance of SuppressionsSucessResponsetBody from a JSON string
suppressions_sucess_responset_body_instance = SuppressionsSucessResponsetBody.from_json(json)
# print the JSON string representation of the object
print SuppressionsSucessResponsetBody.to_json()

# convert the object into a dict
suppressions_sucess_responset_body_dict = suppressions_sucess_responset_body_instance.to_dict()
# create an instance of SuppressionsSucessResponsetBody from a dict
suppressions_sucess_responset_body_form_dict = suppressions_sucess_responset_body.from_dict(suppressions_sucess_responset_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


