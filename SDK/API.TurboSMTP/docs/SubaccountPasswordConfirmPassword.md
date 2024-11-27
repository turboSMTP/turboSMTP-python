# SubaccountPasswordConfirmPassword


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | subaccount password | [optional] 
**confirm_password** | **str** | subaccount confirm password | [optional] 

## Example

```python
from API_TurboSMTP.models.subaccount_password_confirm_password import SubaccountPasswordConfirmPassword

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountPasswordConfirmPassword from a JSON string
subaccount_password_confirm_password_instance = SubaccountPasswordConfirmPassword.from_json(json)
# print the JSON string representation of the object
print SubaccountPasswordConfirmPassword.to_json()

# convert the object into a dict
subaccount_password_confirm_password_dict = subaccount_password_confirm_password_instance.to_dict()
# create an instance of SubaccountPasswordConfirmPassword from a dict
subaccount_password_confirm_password_form_dict = subaccount_password_confirm_password.from_dict(subaccount_password_confirm_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


