# EmailValidatorSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | [**Currency**](Currency.md) |  | 
**free_credits** | **int** | Ammount of allocated free credits. | 
**free_credits_used** | **int** | Ammount of used free credits. | 
**last_used_period** | **str** | Last time credit was used. | 
**latest_period_start_date** | **str** | Free credit period start date (renewed each cycle). | 
**period_expiration_date** | **str** | Free credit period expiration date. | 
**paid_credits** | **float** | Amount of remaining money specified in the &#39;currency&#39; field value currency. | 
**remaining_free_credit** | **int** | Ammount of remaining free credits. | [optional] 

## Example

```python
from API_TurboSMTP.models.email_validator_subscription import EmailValidatorSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of EmailValidatorSubscription from a JSON string
email_validator_subscription_instance = EmailValidatorSubscription.from_json(json)
# print the JSON string representation of the object
print EmailValidatorSubscription.to_json()

# convert the object into a dict
email_validator_subscription_dict = email_validator_subscription_instance.to_dict()
# create an instance of EmailValidatorSubscription from a dict
email_validator_subscription_form_dict = email_validator_subscription.from_dict(email_validator_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


