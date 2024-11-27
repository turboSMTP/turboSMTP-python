# SubAccountListSucessResponsetBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**results** | [**List[SubaccountListItem]**](SubaccountListItem.md) |  | [optional] 

## Example

```python
from API_TurboSMTP.models.sub_account_list_sucess_responset_body import SubAccountListSucessResponsetBody

# TODO update the JSON string below
json = "{}"
# create an instance of SubAccountListSucessResponsetBody from a JSON string
sub_account_list_sucess_responset_body_instance = SubAccountListSucessResponsetBody.from_json(json)
# print the JSON string representation of the object
print SubAccountListSucessResponsetBody.to_json()

# convert the object into a dict
sub_account_list_sucess_responset_body_dict = sub_account_list_sucess_responset_body_instance.to_dict()
# create an instance of SubAccountListSucessResponsetBody from a dict
sub_account_list_sucess_responset_body_form_dict = sub_account_list_sucess_responset_body.from_dict(sub_account_list_sucess_responset_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


