# EmailValidatorList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Email validation list id. | [optional] 
**creation_time** | **str** | Date and Time of the validation list creation. | [optional] 
**file_name** | **str** | File name of the uploaded file. | [optional] 
**is_processed** | **bool** | True if the validation list was already processed. | [optional] 
**percentage** | **int** | Describes the percentage progress of validation list. | [optional] 
**total_emails** | **int** | Amount of email addresses in the validation list. | [optional] 
**total_processed** | **int** | Describes the count of email addresses processed so far. | [optional] 
**status_summary** | [**List[EmailValidatorStatusSummaryItem]**](EmailValidatorStatusSummaryItem.md) |  | [optional] 

## Example

```python
from API_TurboSMTP.models.email_validator_list import EmailValidatorList

# TODO update the JSON string below
json = "{}"
# create an instance of EmailValidatorList from a JSON string
email_validator_list_instance = EmailValidatorList.from_json(json)
# print the JSON string representation of the object
print EmailValidatorList.to_json()

# convert the object into a dict
email_validator_list_dict = email_validator_list_instance.to_dict()
# create an instance of EmailValidatorList from a dict
email_validator_list_form_dict = email_validator_list.from_dict(email_validator_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


