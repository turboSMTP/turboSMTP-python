# SubaccountBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | IP address to use for sending emails. | [optional] 
**first_name** | **str** | subaccount owner first name | [optional] 
**last_name** | **str** | subaccount owner last name | [optional] 
**address_1** | **str** | Address Line 1 | [optional] 
**address_2** | **str** | Address Line 2 | [optional] 
**city** | **str** | City | [optional] 
**company_name** | **str** | Agency Name | [optional] 
**country** | **str** | Country | [optional] 
**region** | **str** | Region | [optional] 
**zip_code** | **str** | Zip Code | [optional] 
**phone_number** | **str** | Phone Number | [optional] 
**policy_agree** | **bool** | Policy must be agreed in order to be able to create a subaccount. | [optional] 
**site_url** | **str** | Website | [optional] 

## Example

```python
from API_TurboSMTP.models.subaccount_base import SubaccountBase

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountBase from a JSON string
subaccount_base_instance = SubaccountBase.from_json(json)
# print the JSON string representation of the object
print SubaccountBase.to_json()

# convert the object into a dict
subaccount_base_dict = subaccount_base_instance.to_dict()
# create an instance of SubaccountBase from a dict
subaccount_base_form_dict = subaccount_base.from_dict(subaccount_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


