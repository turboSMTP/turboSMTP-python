# SuppressionUploadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**valid** | **List[str]** |  | [optional] 
**invalid** | **List[str]** |  | [optional] 

## Example

```python
from API_TurboSMTP.models.suppression_upload_response import SuppressionUploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SuppressionUploadResponse from a JSON string
suppression_upload_response_instance = SuppressionUploadResponse.from_json(json)
# print the JSON string representation of the object
print SuppressionUploadResponse.to_json()

# convert the object into a dict
suppression_upload_response_dict = suppression_upload_response_instance.to_dict()
# create an instance of SuppressionUploadResponse from a dict
suppression_upload_response_form_dict = suppression_upload_response.from_dict(suppression_upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


