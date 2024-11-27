# ConsumerKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumer_key** | **str** | Consumer Key | [optional] 
**label** | **str** | Consumer Key label. | [optional] 
**creation_time** | **str** | The time the consumer key was created. | [optional] 

## Example

```python
from API_TurboSMTP.models.consumer_key import ConsumerKey

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumerKey from a JSON string
consumer_key_instance = ConsumerKey.from_json(json)
# print the JSON string representation of the object
print ConsumerKey.to_json()

# convert the object into a dict
consumer_key_dict = consumer_key_instance.to_dict()
# create an instance of ConsumerKey from a dict
consumer_key_form_dict = consumer_key.from_dict(consumer_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


