# ConsumerKeyListSucessResponsetBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**results** | [**List[ConsumerKey]**](ConsumerKey.md) |  | [optional] 

## Example

```python
from API_TurboSMTP.models.consumer_key_list_sucess_responset_body import ConsumerKeyListSucessResponsetBody

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumerKeyListSucessResponsetBody from a JSON string
consumer_key_list_sucess_responset_body_instance = ConsumerKeyListSucessResponsetBody.from_json(json)
# print the JSON string representation of the object
print ConsumerKeyListSucessResponsetBody.to_json()

# convert the object into a dict
consumer_key_list_sucess_responset_body_dict = consumer_key_list_sucess_responset_body_instance.to_dict()
# create an instance of ConsumerKeyListSucessResponsetBody from a dict
consumer_key_list_sucess_responset_body_form_dict = consumer_key_list_sucess_responset_body.from_dict(consumer_key_list_sucess_responset_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


