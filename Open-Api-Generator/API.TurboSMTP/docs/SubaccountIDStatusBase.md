# SubaccountIDStatusBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | IP address to use for sending emails. | [optional] 
**active** | **bool** | Active subaccounts can be used for login purpose, while users can´t login to inactive subaccounts. Notice that in order to be able to send emails the subaccount subscription must also be active. User can set subaccounts to active / inactive from the dashboard. | 
**subaccount_id** | **int** | Sub account Id | [optional] 
**parent_id** | **int** | Sub account parent Id | [optional] 

## Example

```python
from API_TurboSMTP.models.subaccount_id_status_base import SubaccountIDStatusBase

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountIDStatusBase from a JSON string
subaccount_id_status_base_instance = SubaccountIDStatusBase.from_json(json)
# print the JSON string representation of the object
print SubaccountIDStatusBase.to_json()

# convert the object into a dict
subaccount_id_status_base_dict = subaccount_id_status_base_instance.to_dict()
# create an instance of SubaccountIDStatusBase from a dict
subaccount_id_status_base_form_dict = subaccount_id_status_base.from_dict(subaccount_id_status_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


