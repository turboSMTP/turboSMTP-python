# SubaccountSMTPLimit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The ammount of emails the sub account is allowed to send over the period specified by plan_limit_interval. Value -1 means no limit. | 

## Example

```python
from API_TurboSMTP.models.subaccount_smtp_limit import SubaccountSMTPLimit

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountSMTPLimit from a JSON string
subaccount_smtp_limit_instance = SubaccountSMTPLimit.from_json(json)
# print the JSON string representation of the object
print SubaccountSMTPLimit.to_json()

# convert the object into a dict
subaccount_smtp_limit_dict = subaccount_smtp_limit_instance.to_dict()
# create an instance of SubaccountSMTPLimit from a dict
subaccount_smtp_limit_form_dict = subaccount_smtp_limit.from_dict(subaccount_smtp_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


