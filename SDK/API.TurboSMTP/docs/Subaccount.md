# Subaccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**ip** | **str** | IP address to use for sending emails. | [optional] 
**active** | **bool** | Active subaccounts can be used for login purpose, while users can´t login to inactive subaccounts. Notice that in order to be able to send emails the subaccount subscription must also be active. User can set subaccounts to active / inactive from the dashboard. | 
**subaccount_id** | **int** | Sub account Id | [optional] 
**parent_id** | **int** | Sub account parent Id | [optional] 
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
from API_TurboSMTP.models.subaccount import Subaccount

# TODO update the JSON string below
json = "{}"
# create an instance of Subaccount from a JSON string
subaccount_instance = Subaccount.from_json(json)
# print the JSON string representation of the object
print Subaccount.to_json()

# convert the object into a dict
subaccount_dict = subaccount_instance.to_dict()
# create an instance of Subaccount from a dict
subaccount_form_dict = subaccount.from_dict(subaccount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


