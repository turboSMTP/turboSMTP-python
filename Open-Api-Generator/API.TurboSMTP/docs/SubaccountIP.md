# SubaccountIP


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | IP address to use for sending emails. | [optional] 

## Example

```python
from API_TurboSMTP.models.subaccount_ip import SubaccountIP

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountIP from a JSON string
subaccount_ip_instance = SubaccountIP.from_json(json)
# print the JSON string representation of the object
print SubaccountIP.to_json()

# convert the object into a dict
subaccount_ip_dict = subaccount_ip_instance.to_dict()
# create an instance of SubaccountIP from a dict
subaccount_ip_form_dict = subaccount_ip.from_dict(subaccount_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


