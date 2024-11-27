# EmailRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authuser** | **str** | email of turboSMTP account | [optional] 
**authpass** | **str** | password of turboSMTP account | [optional] 
**var_from** | **str** | from mail address | [optional] 
**to** | **str** | comma-separated recipients emails list | [optional] 
**subject** | **str** | email subject | [optional] 
**cc** | **str** | comma-separated copy emails list | [optional] 
**bcc** | **str** | comma-separated hidden copy emails list | [optional] 
**content** | **str** | text content of the email | [optional] 
**html_content** | **str** | html content of the email | [optional] 
**custom_headers** | **Dict[str, str]** | email additional headers, use any additional header like standard ones List-Unsubscribe (to allow users to easily unsubscribe), X-Entity-Ref-ID (to handle how gmail and other clients group threads), and your own ones.   | [optional] 
**reference_id** | **str** | custom argument included within an email to be added to the Event Webhook response. | [optional] 
**x_campaign_id** | **str** | custom argument included within an email identify the campaign the email belongs to. | [optional] 
**mime_raw** | **str** | mime message which replaces content and hmtl content | [optional] 
**attachments** | [**List[Attachment]**](Attachment.md) | array of attachment objects | [optional] 

## Example

```python
from API_TurboSMTP.models.email_request_body import EmailRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of EmailRequestBody from a JSON string
email_request_body_instance = EmailRequestBody.from_json(json)
# print the JSON string representation of the object
print EmailRequestBody.to_json()

# convert the object into a dict
email_request_body_dict = email_request_body_instance.to_dict()
# create an instance of EmailRequestBody from a dict
email_request_body_form_dict = email_request_body.from_dict(email_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


