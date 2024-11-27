# API_TurboSMTP.MailApi

All URIs are relative to *https://pro.api.serversmtp.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_email**](MailApi.md#send_email) | **POST** /mail/send | Send email message


# **send_email**
> SendSucessResponsetBody send_email(email_request_body)

Send email message

Send email message  ###### **Notes:** **- When using API Keys (suggested authentication method), authuser and authpass properties should not be included.**  **- Switch to \"Complete Email Send Request Body\" sample to learn about advanced features such as using attachments, custom headers like reply-to address, tracking and others.**  ###### Limitations:      * The total size of your email, including attachments, must be less than 24MB. 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.email_request_body import EmailRequestBody
from API_TurboSMTP.models.send_sucess_responset_body import SendSucessResponsetBody
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
    api_instance = API_TurboSMTP.MailApi(api_client)
    email_request_body = {"authuser":"user@example.com","authpass":"SMkhhf4J68XX","from":"user@example.com","to":"user@example.com,user2@example.com","subject":"This is a test message","cc":"cc_user@example.com","bcc":"bcc_user@example.com","content":"This is plain text version of the message.","html_content":"This is <b>HTML</b> version of the message."} # EmailRequestBody | 

    try:
        # Send email message
        api_response = api_instance.send_email(email_request_body)
        print("The response of MailApi->send_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailApi->send_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_request_body** | [**EmailRequestBody**](EmailRequestBody.md)|  | 

### Return type

[**SendSucessResponsetBody**](SendSucessResponsetBody.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sucess  Turbo-SMTP successfully received your message.  |  -  |
**400** | Bad Request  There was a problem processing the request due to an invalid/missing parameter for the request.  |  -  |
**401** | Unauthorized  Missing or Invalid Turbo-SMTP credentials provided.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

