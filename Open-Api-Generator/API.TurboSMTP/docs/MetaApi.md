# API_TurboSMTP.MetaApi

All URIs are relative to *https://pro.api.serversmtp.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_countries**](MetaApi.md#get_countries) | **GET** /meta/countries | Get countries
[**get_states_by_country**](MetaApi.md#get_states_by_country) | **GET** /meta/state/{isoCode} | Get states by country


# **get_countries**
> List[Country] get_countries()

Get countries

Get countries 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.country import Country
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
    api_instance = API_TurboSMTP.MetaApi(api_client)

    try:
        # Get countries
        api_response = api_instance.get_countries()
        print("The response of MetaApi->get_countries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaApi->get_countries: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Country]**](Country.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Countries list |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_states_by_country**
> List[State] get_states_by_country(iso_code)

Get states by country

Get states by country 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.state import State
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
    api_instance = API_TurboSMTP.MetaApi(api_client)
    iso_code = 'ES' # str | Country ISO code

    try:
        # Get states by country
        api_response = api_instance.get_states_by_country(iso_code)
        print("The response of MetaApi->get_states_by_country:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaApi->get_states_by_country: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iso_code** | **str**| Country ISO code | 

### Return type

[**List[State]**](State.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | States selected |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |
**404** | Not Found  Please verify the Country Iso Code Provided.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

