# API_TurboSMTP.ConsumerkeyApi

All URIs are relative to *https://pro.api.serversmtp.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_consumer_key**](ConsumerkeyApi.md#create_consumer_key) | **POST** /user/consumerKeys | Create Consumer Key
[**delete_consumer_key**](ConsumerkeyApi.md#delete_consumer_key) | **DELETE** /user/consumerKeys/{consumerKey} | Delete Consumer Key
[**list_consumer_keys**](ConsumerkeyApi.md#list_consumer_keys) | **GET** /user/consumerKeys | Get Consumer Keys list


# **create_consumer_key**
> ConsumerKeyCreateResponseBody create_consumer_key(consumer_key_create_request_body)

Create Consumer Key

 Create new Consumer Key  Note: Consumer Key creation is not allwed when authenticated via Consumer Key. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import API_TurboSMTP
from API_TurboSMTP.models.consumer_key_create_request_body import ConsumerKeyCreateRequestBody
from API_TurboSMTP.models.consumer_key_create_response_body import ConsumerKeyCreateResponseBody
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with API_TurboSMTP.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = API_TurboSMTP.ConsumerkeyApi(api_client)
    consumer_key_create_request_body = API_TurboSMTP.ConsumerKeyCreateRequestBody() # ConsumerKeyCreateRequestBody | 

    try:
        # Create Consumer Key
        api_response = api_instance.create_consumer_key(consumer_key_create_request_body)
        print("The response of ConsumerkeyApi->create_consumer_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsumerkeyApi->create_consumer_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_key_create_request_body** | [**ConsumerKeyCreateRequestBody**](ConsumerKeyCreateRequestBody.md)|  | 

### Return type

[**ConsumerKeyCreateResponseBody**](ConsumerKeyCreateResponseBody.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Sucess  Consumer Key Created Sucessfully.  |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_consumer_key**
> CommonSuccessResponseBody delete_consumer_key(consumer_key)

Delete Consumer Key

 Delete Consumer Key Note: Consumer Key deletion is not allwed when authenticated via Comsumer Key. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import API_TurboSMTP
from API_TurboSMTP.models.common_success_response_body import CommonSuccessResponseBody
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with API_TurboSMTP.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = API_TurboSMTP.ConsumerkeyApi(api_client)
    consumer_key = 'b914ad238d0e8e8851b81e86ce46ae1d' # str | Consumer Key

    try:
        # Delete Consumer Key
        api_response = api_instance.delete_consumer_key(consumer_key)
        print("The response of ConsumerkeyApi->delete_consumer_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsumerkeyApi->delete_consumer_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_key** | **str**| Consumer Key | 

### Return type

[**CommonSuccessResponseBody**](CommonSuccessResponseBody.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sucess  Consumer Key was deleted.  |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |
**404** | Not Found  Please verify the Consumer Key is valid.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_consumer_keys**
> ConsumerKeyListSucessResponsetBody list_consumer_keys()

Get Consumer Keys list

 Get Consumer Keys list  Note: Consumer Keys listing is not allwed when authenticated via Consumer Key. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import API_TurboSMTP
from API_TurboSMTP.models.consumer_key_list_sucess_responset_body import ConsumerKeyListSucessResponsetBody
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with API_TurboSMTP.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = API_TurboSMTP.ConsumerkeyApi(api_client)

    try:
        # Get Consumer Keys list
        api_response = api_instance.list_consumer_keys()
        print("The response of ConsumerkeyApi->list_consumer_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsumerkeyApi->list_consumer_keys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ConsumerKeyListSucessResponsetBody**](ConsumerKeyListSucessResponsetBody.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sucess  Consumer Keys list  |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

