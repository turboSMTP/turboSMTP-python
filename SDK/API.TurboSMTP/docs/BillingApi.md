# API_TurboSMTP.BillingApi

All URIs are relative to *https://pro.api.serversmtp.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buy_email_validator_credits**](BillingApi.md#buy_email_validator_credits) | **POST** /billing/buy_emailvalidation_credits | Buy Email Validator Credits


# **buy_email_validator_credits**
> BuyEmailValidatorCreditsSucessResponse buy_email_validator_credits(buy_email_validator_credits_request)

Buy Email Validator Credits

 Buy Email Validator Credits 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.buy_email_validator_credits_request import BuyEmailValidatorCreditsRequest
from API_TurboSMTP.models.buy_email_validator_credits_sucess_response import BuyEmailValidatorCreditsSucessResponse
from API_TurboSMTP.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://pro.api.serversmtp.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = API_TurboSMTP.Configuration(
    host = "https://pro.api.serversmtp.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: consumerSecret
configuration.api_key['consumerSecret'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['consumerSecret'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure API key authorization: consumerKey
configuration.api_key['consumerKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['consumerKey'] = 'Bearer'

# Enter a context with an instance of the API client
with API_TurboSMTP.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = API_TurboSMTP.BillingApi(api_client)
    buy_email_validator_credits_request = API_TurboSMTP.BuyEmailValidatorCreditsRequest() # BuyEmailValidatorCreditsRequest | 

    try:
        # Buy Email Validator Credits
        api_response = api_instance.buy_email_validator_credits(buy_email_validator_credits_request)
        print("The response of BillingApi->buy_email_validator_credits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->buy_email_validator_credits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buy_email_validator_credits_request** | [**BuyEmailValidatorCreditsRequest**](BuyEmailValidatorCreditsRequest.md)|  | 

### Return type

[**BuyEmailValidatorCreditsSucessResponse**](BuyEmailValidatorCreditsSucessResponse.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sucess  Returns url to the billing system to allow payment completition.   |  -  |
**400** | Bad Request  ###### Produces:  * missing_required_parameter_amount * amount_should_be_integer * amount_should_not_be_less_than_15 * amount_should_not_be_higher_than_1800 * can_not_buy_extra_credit_without_active_plan  |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

