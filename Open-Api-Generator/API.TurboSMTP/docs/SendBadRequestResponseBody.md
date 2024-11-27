# SendBadRequestResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**errors** | **List[str]** |  | [optional] 

## Example

```python
from API_TurboSMTP.models.send_bad_request_response_body import SendBadRequestResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of SendBadRequestResponseBody from a JSON string
send_bad_request_response_body_instance = SendBadRequestResponseBody.from_json(json)
# print the JSON string representation of the object
print SendBadRequestResponseBody.to_json()

# convert the object into a dict
send_bad_request_response_body_dict = send_bad_request_response_body_instance.to_dict()
# create an instance of SendBadRequestResponseBody from a dict
send_bad_request_response_body_form_dict = send_bad_request_response_body.from_dict(send_bad_request_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


