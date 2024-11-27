# AnalyticMailItem

Sent Email

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Email Id. | [optional] 
**subject** | **str** | Email Subject. | [optional] 
**sender** | **str** | Email Sender. | [optional] 
**recipient** | **str** | Email Recipient. | [optional] 
**send_time** | **str** | Date Time email was sent. | [optional] 
**status** | [**AnalyticMailStatus**](AnalyticMailStatus.md) |  | [optional] 
**domain** | **str** | The portion of the sender´s email address after the \&quot;@\&quot; symbol. | [optional] 
**contact_domain** | **str** | The portion of the recipient´s email address after the \&quot;@\&quot; symbol. | [optional] 
**x_campaign_id** | **str** | Value specified in the x_campaign_id custom header to track campaigns specific data. | [optional] 
**error** | **str** | Error returned when delivering the email message. | [optional] 

## Example

```python
from API_TurboSMTP.models.analytic_mail_item import AnalyticMailItem

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticMailItem from a JSON string
analytic_mail_item_instance = AnalyticMailItem.from_json(json)
# print the JSON string representation of the object
print AnalyticMailItem.to_json()

# convert the object into a dict
analytic_mail_item_dict = analytic_mail_item_instance.to_dict()
# create an instance of AnalyticMailItem from a dict
analytic_mail_item_form_dict = analytic_mail_item.from_dict(analytic_mail_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


