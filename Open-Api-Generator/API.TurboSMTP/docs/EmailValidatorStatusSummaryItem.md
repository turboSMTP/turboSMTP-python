# EmailValidatorStatusSummaryItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  The status of the email address you are validating.    DELIVERABILITY STATUS EXPLANATION    valid:   These are emails that were determined to be valid and safe to email to, they will have a very low bounce rate of under 2%. If you receive bounces it can be because your IP might be blacklisted where our IP was not. Sometimes the email accounts exist, but they are only accepting mail from people in their contact lists. Sometimes you will get throttle on number of emails you can send to a specific domain per hour. It&#39;s important to look at the SMTP Bounce codes to determine why.      invalid:   These are emails that were determined to be invalid, please delete them from your mailing list.      catch-all:    These emails are impossible to validate without sending a real email and waiting for a bounce. The term Catch-all means that the email server tells you that the email is valid, whether it&#39;s valid or invalid. If you want to email these addresses, we suggest you segment them into a catch-all group and be aware that some of these will most likely bounce.      spamtrap:    These emails are believed to be spamtraps and should not be mailed. We have technology in place to determine if certain emails should be classified as spamtrap. We don&#39;t know all the spamtrap email addresses, but we do know a lot of them.      abuse:    These emails belong to people who are known to click the abuse links in emails, hence abusers or complainers. We recommend not emailing these addresses.      do_not_mail:    These emails belong to companies, role-based, or people you just want to avoid emailing to. They are broken down into 6 sub-categories \&quot;disposable\&quot;,\&quot;toxic\&quot;, \&quot;role_based\&quot;, \&quot;role_based_catch_all\&quot;, \&quot;global_suppression\&quot; and \&quot;possible_trap\&quot;. You should decide if you want to email these address. They are valid email addresses, but shouldn&#39;t be mailed in most cases.      unknown:    These emails we weren&#39;t able to validate for one reason or another. Typical cases are \&quot;Their mail server was down\&quot; or \&quot;the anti-spam system is blocking us\&quot;. In most cases, 80% unknowns are invalid/bad email addresses.  | [optional] 
**total** | **int** | Ammount of emails in the status within the list. | [optional] 

## Example

```python
from API_TurboSMTP.models.email_validator_status_summary_item import EmailValidatorStatusSummaryItem

# TODO update the JSON string below
json = "{}"
# create an instance of EmailValidatorStatusSummaryItem from a JSON string
email_validator_status_summary_item_instance = EmailValidatorStatusSummaryItem.from_json(json)
# print the JSON string representation of the object
print EmailValidatorStatusSummaryItem.to_json()

# convert the object into a dict
email_validator_status_summary_item_dict = email_validator_status_summary_item_instance.to_dict()
# create an instance of EmailValidatorStatusSummaryItem from a dict
email_validator_status_summary_item_form_dict = email_validator_status_summary_item.from_dict(email_validator_status_summary_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


