# SubaccountActiveStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Active subaccounts can be used for login purpose, while users can´t login to inactive subaccounts. Notice that in order to be able to send emails the subaccount subscription must also be active. User can set subaccounts to active / inactive from the dashboard. | 

## Example

```python
from API_TurboSMTP.models.subaccount_active_status import SubaccountActiveStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountActiveStatus from a JSON string
subaccount_active_status_instance = SubaccountActiveStatus.from_json(json)
# print the JSON string representation of the object
print SubaccountActiveStatus.to_json()

# convert the object into a dict
subaccount_active_status_dict = subaccount_active_status_instance.to_dict()
# create an instance of SubaccountActiveStatus from a dict
subaccount_active_status_form_dict = subaccount_active_status.from_dict(subaccount_active_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


