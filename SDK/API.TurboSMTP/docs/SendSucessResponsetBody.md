# SendSucessResponsetBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**mid** | **int** | message ID | [optional] 

## Example

```python
from API_TurboSMTP.models.send_sucess_responset_body import SendSucessResponsetBody

# TODO update the JSON string below
json = "{}"
# create an instance of SendSucessResponsetBody from a JSON string
send_sucess_responset_body_instance = SendSucessResponsetBody.from_json(json)
# print the JSON string representation of the object
print SendSucessResponsetBody.to_json()

# convert the object into a dict
send_sucess_responset_body_dict = send_sucess_responset_body_instance.to_dict()
# create an instance of SendSucessResponsetBody from a dict
send_sucess_responset_body_form_dict = send_sucess_responset_body.from_dict(send_sucess_responset_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


