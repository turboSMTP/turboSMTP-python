# EmailValidatorSucessResponsetBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**results** | [**List[EmailValidatorList]**](EmailValidatorList.md) |  | [optional] 

## Example

```python
from API_TurboSMTP.models.email_validator_sucess_responset_body import EmailValidatorSucessResponsetBody

# TODO update the JSON string below
json = "{}"
# create an instance of EmailValidatorSucessResponsetBody from a JSON string
email_validator_sucess_responset_body_instance = EmailValidatorSucessResponsetBody.from_json(json)
# print the JSON string representation of the object
print EmailValidatorSucessResponsetBody.to_json()

# convert the object into a dict
email_validator_sucess_responset_body_dict = email_validator_sucess_responset_body_instance.to_dict()
# create an instance of EmailValidatorSucessResponsetBody from a dict
email_validator_sucess_responset_body_form_dict = email_validator_sucess_responset_body.from_dict(email_validator_sucess_responset_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


