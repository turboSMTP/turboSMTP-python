# ConsumerKeyCreateResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumer_key** | **str** | Consumer Key | [optional] 
**consumer_secret** | **str** | Consumer Secret | [optional] 

## Example

```python
from API_TurboSMTP.models.consumer_key_create_response_body import ConsumerKeyCreateResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumerKeyCreateResponseBody from a JSON string
consumer_key_create_response_body_instance = ConsumerKeyCreateResponseBody.from_json(json)
# print the JSON string representation of the object
print ConsumerKeyCreateResponseBody.to_json()

# convert the object into a dict
consumer_key_create_response_body_dict = consumer_key_create_response_body_instance.to_dict()
# create an instance of ConsumerKeyCreateResponseBody from a dict
consumer_key_create_response_body_form_dict = consumer_key_create_response_body.from_dict(consumer_key_create_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


