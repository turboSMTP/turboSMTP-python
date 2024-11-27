# EmailValidationUploadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_id** | **int** | List Identifier | [optional] 
**total_emails** | **int** | Total emails found in uploaded file | [optional] 

## Example

```python
from API_TurboSMTP.models.email_validation_upload_response import EmailValidationUploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailValidationUploadResponse from a JSON string
email_validation_upload_response_instance = EmailValidationUploadResponse.from_json(json)
# print the JSON string representation of the object
print EmailValidationUploadResponse.to_json()

# convert the object into a dict
email_validation_upload_response_dict = email_validation_upload_response_instance.to_dict()
# create an instance of EmailValidationUploadResponse from a dict
email_validation_upload_response_form_dict = email_validation_upload_response.from_dict(email_validation_upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


