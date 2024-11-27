# SubaccountCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
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
**password** | **str** | subaccount password | 
**confirm_password** | **str** | subaccount confirm password | 

## Example

```python
from API_TurboSMTP.models.subaccount_create_request import SubaccountCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountCreateRequest from a JSON string
subaccount_create_request_instance = SubaccountCreateRequest.from_json(json)
# print the JSON string representation of the object
print SubaccountCreateRequest.to_json()

# convert the object into a dict
subaccount_create_request_dict = subaccount_create_request_instance.to_dict()
# create an instance of SubaccountCreateRequest from a dict
subaccount_create_request_form_dict = subaccount_create_request.from_dict(subaccount_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


