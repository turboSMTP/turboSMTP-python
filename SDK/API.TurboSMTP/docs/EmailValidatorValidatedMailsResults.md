# EmailValidatorValidatedMailsResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Count of vaidated email addresses in the list. | [optional] 
**processed** | **int** | Number of processed email addresses in the list. | [optional] 
**results** | [**List[EmailValidatorMailDetailsBasic]**](EmailValidatorMailDetailsBasic.md) | Array of validated email addresses in the list. | [optional] 

## Example

```python
from API_TurboSMTP.models.email_validator_validated_mails_results import EmailValidatorValidatedMailsResults

# TODO update the JSON string below
json = "{}"
# create an instance of EmailValidatorValidatedMailsResults from a JSON string
email_validator_validated_mails_results_instance = EmailValidatorValidatedMailsResults.from_json(json)
# print the JSON string representation of the object
print EmailValidatorValidatedMailsResults.to_json()

# convert the object into a dict
email_validator_validated_mails_results_dict = email_validator_validated_mails_results_instance.to_dict()
# create an instance of EmailValidatorValidatedMailsResults from a dict
email_validator_validated_mails_results_form_dict = email_validator_validated_mails_results.from_dict(email_validator_validated_mails_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


