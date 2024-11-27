# SubaccountUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | IP address to use for sending emails. | 
**first_name** | **str** | subaccount owner first name | 
**last_name** | **str** | subaccount owner last name | 
**address_1** | **str** | Address Line 1 | [optional] 
**address_2** | **str** | Address Line 2 | [optional] 
**city** | **str** | City | [optional] 
**company_name** | **str** | Agency Name | [optional] 
**country** | **str** | Country | [optional] 
**region** | **str** | Region | [optional] 
**zip_code** | **str** | Zip Code | [optional] 
**phone_number** | **str** | Phone Number | [optional] 
**policy_agree** | **bool** | Policy must be agreed in order to be able to create a subaccount. | 
**site_url** | **str** | Website | [optional] 
**password** | **str** | subaccount password | [optional] 
**confirm_password** | **str** | subaccount confirm password | [optional] 

## Example

```python
from API_TurboSMTP.models.subaccount_update_request import SubaccountUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountUpdateRequest from a JSON string
subaccount_update_request_instance = SubaccountUpdateRequest.from_json(json)
# print the JSON string representation of the object
print SubaccountUpdateRequest.to_json()

# convert the object into a dict
subaccount_update_request_dict = subaccount_update_request_instance.to_dict()
# create an instance of SubaccountUpdateRequest from a dict
subaccount_update_request_form_dict = subaccount_update_request.from_dict(subaccount_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


