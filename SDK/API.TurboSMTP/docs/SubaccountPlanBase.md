# SubaccountPlanBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The ammount of emails the sub account is allowed to send over the period specified by plan_limit_interval. Value -1 means no limit. | 
**sent** | **int** | The ammount of sent emails from the sub account over the current period. | [optional] 
**last_used** | **str** | The date time the sub account was last used. | [optional] 
**plan_expiration** | **str** | Expiration date time of the plan. | [optional] 
**plan_limit_interval** | [**SmtpLimitInterval**](SmtpLimitInterval.md) |  | [optional] 
**expired** | **bool** | Expired if plan expiration date is overdue. | [optional] 

## Example

```python
from API_TurboSMTP.models.subaccount_plan_base import SubaccountPlanBase

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountPlanBase from a JSON string
subaccount_plan_base_instance = SubaccountPlanBase.from_json(json)
# print the JSON string representation of the object
print SubaccountPlanBase.to_json()

# convert the object into a dict
subaccount_plan_base_dict = subaccount_plan_base_instance.to_dict()
# create an instance of SubaccountPlanBase from a dict
subaccount_plan_base_form_dict = subaccount_plan_base.from_dict(subaccount_plan_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


