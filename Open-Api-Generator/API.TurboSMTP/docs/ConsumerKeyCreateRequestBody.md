# ConsumerKeyCreateRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Consumer Key label. | [optional] 

## Example

```python
from API_TurboSMTP.models.consumer_key_create_request_body import ConsumerKeyCreateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumerKeyCreateRequestBody from a JSON string
consumer_key_create_request_body_instance = ConsumerKeyCreateRequestBody.from_json(json)
# print the JSON string representation of the object
print ConsumerKeyCreateRequestBody.to_json()

# convert the object into a dict
consumer_key_create_request_body_dict = consumer_key_create_request_body_instance.to_dict()
# create an instance of ConsumerKeyCreateRequestBody from a dict
consumer_key_create_request_body_form_dict = consumer_key_create_request_body.from_dict(consumer_key_create_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


