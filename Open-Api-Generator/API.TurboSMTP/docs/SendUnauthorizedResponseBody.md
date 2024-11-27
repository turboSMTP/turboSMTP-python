# SendUnauthorizedResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**details** | **str** |  | [optional] 

## Example

```python
from API_TurboSMTP.models.send_unauthorized_response_body import SendUnauthorizedResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of SendUnauthorizedResponseBody from a JSON string
send_unauthorized_response_body_instance = SendUnauthorizedResponseBody.from_json(json)
# print the JSON string representation of the object
print SendUnauthorizedResponseBody.to_json()

# convert the object into a dict
send_unauthorized_response_body_dict = send_unauthorized_response_body_instance.to_dict()
# create an instance of SendUnauthorizedResponseBody from a dict
send_unauthorized_response_body_form_dict = send_unauthorized_response_body.from_dict(send_unauthorized_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


