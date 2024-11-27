# BaseAgencySettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agency_name** | **str** | Agency Name | [optional] 
**agency_website** | **str** | Agency Website | [optional] 
**agency_footer** | **str** | Footer to be used | [optional] 

## Example

```python
from API_TurboSMTP.models.base_agency_settings import BaseAgencySettings

# TODO update the JSON string below
json = "{}"
# create an instance of BaseAgencySettings from a JSON string
base_agency_settings_instance = BaseAgencySettings.from_json(json)
# print the JSON string representation of the object
print BaseAgencySettings.to_json()

# convert the object into a dict
base_agency_settings_dict = base_agency_settings_instance.to_dict()
# create an instance of BaseAgencySettings from a dict
base_agency_settings_form_dict = base_agency_settings.from_dict(base_agency_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


