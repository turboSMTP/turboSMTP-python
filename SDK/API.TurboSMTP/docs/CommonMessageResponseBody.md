# CommonMessageResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 

## Example

```python
from API_TurboSMTP.models.common_message_response_body import CommonMessageResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of CommonMessageResponseBody from a JSON string
common_message_response_body_instance = CommonMessageResponseBody.from_json(json)
# print the JSON string representation of the object
print CommonMessageResponseBody.to_json()

# convert the object into a dict
common_message_response_body_dict = common_message_response_body_instance.to_dict()
# create an instance of CommonMessageResponseBody from a dict
common_message_response_body_form_dict = common_message_response_body.from_dict(common_message_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


