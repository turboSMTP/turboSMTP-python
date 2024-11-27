# API_TurboSMTP.AlertsApi

All URIs are relative to *https://pro.api.serversmtp.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_alert**](AlertsApi.md#create_alert) | **POST** /tools/alerts | Create new Alert Notification
[**delete_alert**](AlertsApi.md#delete_alert) | **DELETE** /tools/alerts/{Id} | Delete Alert Notification
[**get_alert**](AlertsApi.md#get_alert) | **GET** /tools/alerts/{Id} | Get Alert Notification
[**get_alerts**](AlertsApi.md#get_alerts) | **GET** /tools/alerts | Get Alerts Notifications Information
[**update_alert**](AlertsApi.md#update_alert) | **PATCH** /tools/alerts/{Id} | Update Alert Notification


# **create_alert**
> Alert create_alert(alert_base)

Create new Alert Notification

 Create new Alert Notification 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.alert import Alert
from API_TurboSMTP.models.alert_base import AlertBase
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
    api_instance = API_TurboSMTP.AlertsApi(api_client)
    alert_base = API_TurboSMTP.AlertBase() # AlertBase | 

    try:
        # Create new Alert Notification
        api_response = api_instance.create_alert(alert_base)
        print("The response of AlertsApi->create_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->create_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_base** | [**AlertBase**](AlertBase.md)|  | 

### Return type

[**Alert**](Alert.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Sucess  Alert Notification Created Sucessfully.  |  -  |
**400** | Bad Request  ###### Produces:  * missing_required_parameter_email * missing_required_parameter_percentage * percentage_should_be_integer * percentage_should_not_be_less_than_0 * percentage_should_not_be_higher_than_100  |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert**
> CommonSuccessResponseBody delete_alert(id)

Delete Alert Notification

 Delete an Alert Notification. 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

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
    api_instance = API_TurboSMTP.AlertsApi(api_client)
    id = 56 # int | Id

    try:
        # Delete Alert Notification
        api_response = api_instance.delete_alert(id)
        print("The response of AlertsApi->delete_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->delete_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id | 

### Return type

[**CommonSuccessResponseBody**](CommonSuccessResponseBody.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sucess  Alert was deleted.  |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |
**404** | Not Found  Please verify the alert id exists.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert**
> Alert get_alert(id)

Get Alert Notification

 Get Alert Notification. 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.alert import Alert
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
    api_instance = API_TurboSMTP.AlertsApi(api_client)
    id = 56 # int | Id

    try:
        # Get Alert Notification
        api_response = api_instance.get_alert(id)
        print("The response of AlertsApi->get_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->get_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id | 

### Return type

[**Alert**](Alert.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sucess  Alert Notification.  |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |
**404** | Not Found  Please verify the alert id exists.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerts**
> AlertListSucessResponsetBody get_alerts()

Get Alerts Notifications Information

 List Alerts Notifications Information 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.alert_list_sucess_responset_body import AlertListSucessResponsetBody
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
    api_instance = API_TurboSMTP.AlertsApi(api_client)

    try:
        # Get Alerts Notifications Information
        api_response = api_instance.get_alerts()
        print("The response of AlertsApi->get_alerts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->get_alerts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AlertListSucessResponsetBody**](AlertListSucessResponsetBody.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sucess  Alerts list.  |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert**
> Alert update_alert(id, alert_base)

Update Alert Notification

 Update Alert Notification. 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.alert import Alert
from API_TurboSMTP.models.alert_base import AlertBase
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
    api_instance = API_TurboSMTP.AlertsApi(api_client)
    id = 56 # int | Id
    alert_base = API_TurboSMTP.AlertBase() # AlertBase | 

    try:
        # Update Alert Notification
        api_response = api_instance.update_alert(id, alert_base)
        print("The response of AlertsApi->update_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->update_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id | 
 **alert_base** | [**AlertBase**](AlertBase.md)|  | 

### Return type

[**Alert**](Alert.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sucess  Alert updated sucessfully.  |  -  |
**400** | Bad Request  ###### Produces:  * percentage_should_be_integer * percentage_should_not_be_less_than_0 * percentage_should_not_be_higher_than_100  |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |
**404** | Not Found  Please verify the alert id exists.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

