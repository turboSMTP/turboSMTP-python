# SuppressionImportJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**reason** | **str** | Specifies a reason for suppressing imported email address/addresses | [optional] 
**content** | **List[str]** | List of email addresses to suppress. | [optional] 

## Example

```python
from API_TurboSMTP.models.suppression_import_json import SuppressionImportJson

# TODO update the JSON string below
json = "{}"
# create an instance of SuppressionImportJson from a JSON string
suppression_import_json_instance = SuppressionImportJson.from_json(json)
# print the JSON string representation of the object
print SuppressionImportJson.to_json()

# convert the object into a dict
suppression_import_json_dict = suppression_import_json_instance.to_dict()
# create an instance of SuppressionImportJson from a dict
suppression_import_json_form_dict = suppression_import_json.from_dict(suppression_import_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


