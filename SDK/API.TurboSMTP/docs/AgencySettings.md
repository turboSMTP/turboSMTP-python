# AgencySettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logo_url** | **str** |  | [optional] 
**agency_name** | **str** | Agency Name | [optional] 
**agency_website** | **str** | Agency Website | [optional] 
**agency_footer** | **str** | Footer to be used | [optional] 

## Example

```python
from API_TurboSMTP.models.agency_settings import AgencySettings

# TODO update the JSON string below
json = "{}"
# create an instance of AgencySettings from a JSON string
agency_settings_instance = AgencySettings.from_json(json)
# print the JSON string representation of the object
print AgencySettings.to_json()

# convert the object into a dict
agency_settings_dict = agency_settings_instance.to_dict()
# create an instance of AgencySettings from a dict
agency_settings_form_dict = agency_settings.from_dict(agency_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


