# SubaccountListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**ip** | **str** | IP address to use for sending emails. | [optional] 
**active** | **bool** | Active subaccounts can be used for login purpose, while users can´t login to inactive subaccounts. Notice that in order to be able to send emails the subaccount subscription must also be active. User can set subaccounts to active / inactive from the dashboard. | 
**subaccount_id** | **int** | Sub account Id | [optional] 
**parent_id** | **int** | Sub account parent Id | [optional] 
**limit** | **int** | The ammount of emails the sub account is allowed to send over the period specified by plan_limit_interval. Value -1 means no limit. | 
**sent** | **int** | The ammount of sent emails from the sub account over the current period. | [optional] 
**last_used** | **str** | The date time the sub account was last used. | [optional] 
**plan_expiration** | **str** | Expiration date time of the plan. | [optional] 
**plan_limit_interval** | [**SmtpLimitInterval**](SmtpLimitInterval.md) |  | [optional] 
**expired** | **bool** | Expired if plan expiration date is overdue. | [optional] 

## Example

```python
from API_TurboSMTP.models.subaccount_list_item import SubaccountListItem

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountListItem from a JSON string
subaccount_list_item_instance = SubaccountListItem.from_json(json)
# print the JSON string representation of the object
print SubaccountListItem.to_json()

# convert the object into a dict
subaccount_list_item_dict = subaccount_list_item_instance.to_dict()
# create an instance of SubaccountListItem from a dict
subaccount_list_item_form_dict = subaccount_list_item.from_dict(subaccount_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


