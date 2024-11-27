# API_TurboSMTP.SuppressionsApi

All URIs are relative to *https://pro.api.serversmtp.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_delete_suppressions**](SuppressionsApi.md#bulk_delete_suppressions) | **POST** /suppressions/bulk_delete | Bulk delete suppressions
[**delete_filter_suppressions**](SuppressionsApi.md#delete_filter_suppressions) | **POST** /suppressions/delete | Delete suppressions
[**export_filter_suppressions**](SuppressionsApi.md#export_filter_suppressions) | **POST** /suppressions/csv | Export filtered suppressions
[**export_suppressions_data_csv**](SuppressionsApi.md#export_suppressions_data_csv) | **GET** /suppressions/csv | Export Suppressions data in CSV file
[**filter_suppressions**](SuppressionsApi.md#filter_suppressions) | **POST** /suppressions | Filter suppressions
[**get_suppressions**](SuppressionsApi.md#get_suppressions) | **GET** /suppressions | Get Suppressions Data
[**import_suppressions**](SuppressionsApi.md#import_suppressions) | **POST** /suppressions/import | Import Suppressions


# **bulk_delete_suppressions**
> SuppressionsDeleteSuccess bulk_delete_suppressions(request_body)

Bulk delete suppressions

Bulk delete suppressions 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.suppressions_delete_success import SuppressionsDeleteSuccess
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
    api_instance = API_TurboSMTP.SuppressionsApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Bulk delete suppressions
        api_response = api_instance.bulk_delete_suppressions(request_body)
        print("The response of SuppressionsApi->bulk_delete_suppressions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionsApi->bulk_delete_suppressions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 

### Return type

[**SuppressionsDeleteSuccess**](SuppressionsDeleteSuccess.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Suppressions were sucessfully deleted. |  -  |
**400** | Bad Request  ###### Produces:  * no_contacts_were_provided  |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_filter_suppressions**
> SuppressionsDeleteSuccess delete_filter_suppressions(suppression_filter_request_body)

Delete suppressions

Delete suppressions 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.suppression_filter_request_body import SuppressionFilterRequestBody
from API_TurboSMTP.models.suppressions_delete_success import SuppressionsDeleteSuccess
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
    api_instance = API_TurboSMTP.SuppressionsApi(api_client)
    suppression_filter_request_body = API_TurboSMTP.SuppressionFilterRequestBody() # SuppressionFilterRequestBody | 

    try:
        # Delete suppressions
        api_response = api_instance.delete_filter_suppressions(suppression_filter_request_body)
        print("The response of SuppressionsApi->delete_filter_suppressions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionsApi->delete_filter_suppressions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suppression_filter_request_body** | [**SuppressionFilterRequestBody**](SuppressionFilterRequestBody.md)|  | 

### Return type

[**SuppressionsDeleteSuccess**](SuppressionsDeleteSuccess.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | deleted |  -  |
**400** | Bad Request  ###### Produces:  *   |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_filter_suppressions**
> str export_filter_suppressions(suppression_filter_request_body)

Export filtered suppressions

Export Filtered Suppressions 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.suppression_filter_request_body import SuppressionFilterRequestBody
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
    api_instance = API_TurboSMTP.SuppressionsApi(api_client)
    suppression_filter_request_body = API_TurboSMTP.SuppressionFilterRequestBody() # SuppressionFilterRequestBody | 

    try:
        # Export filtered suppressions
        api_response = api_instance.export_filter_suppressions(suppression_filter_request_body)
        print("The response of SuppressionsApi->export_filter_suppressions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionsApi->export_filter_suppressions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suppression_filter_request_body** | [**SuppressionFilterRequestBody**](SuppressionFilterRequestBody.md)|  | 

### Return type

**str**

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/csv, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Suppressions CSV data |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_suppressions_data_csv**
> str export_suppressions_data_csv(var_from, to, tz=tz, filter=filter, filter_by=filter_by, smart_search=smart_search, orderby=orderby, ordertype=ordertype)

Export Suppressions data in CSV file

Export Suppressions data in CSV file 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.list[suppression_source] import List[SuppressionSource]
from API_TurboSMTP.models.order_type import OrderType
from API_TurboSMTP.models.suppression_order_by import SuppressionOrderBy
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
    api_instance = API_TurboSMTP.SuppressionsApi(api_client)
    var_from = '2020-01-01' # date | Start date
    to = '2025-12-31' # date | End date
    tz = '-07:00' # str | Timezone Offset (optional)
    filter = 'Jhon.Doe@gmail.com' # str | Text to search (recipient, sender, email subject or reason for suppression) (optional)
    filter_by = API_TurboSMTP.SuppressionSource() # List[SuppressionSource] |  (optional)
    smart_search = False # bool | Smart search (optional) (default to False)
    orderby = API_TurboSMTP.SuppressionOrderBy() # SuppressionOrderBy |  (optional)
    ordertype = API_TurboSMTP.OrderType() # OrderType |  (optional)

    try:
        # Export Suppressions data in CSV file
        api_response = api_instance.export_suppressions_data_csv(var_from, to, tz=tz, filter=filter, filter_by=filter_by, smart_search=smart_search, orderby=orderby, ordertype=ordertype)
        print("The response of SuppressionsApi->export_suppressions_data_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionsApi->export_suppressions_data_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **date**| Start date | 
 **to** | **date**| End date | 
 **tz** | **str**| Timezone Offset | [optional] 
 **filter** | **str**| Text to search (recipient, sender, email subject or reason for suppression) | [optional] 
 **filter_by** | [**List[SuppressionSource]**](SuppressionSource.md)|  | [optional] 
 **smart_search** | **bool**| Smart search | [optional] [default to False]
 **orderby** | [**SuppressionOrderBy**](.md)|  | [optional] 
 **ordertype** | [**OrderType**](.md)|  | [optional] 

### Return type

**str**

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Suppressions CSV data |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_suppressions**
> SuppressionsSucessResponsetBody filter_suppressions(suppression_filter_order_page_request_body)

Filter suppressions

Get Suppressions Data 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.suppression_filter_order_page_request_body import SuppressionFilterOrderPageRequestBody
from API_TurboSMTP.models.suppressions_sucess_responset_body import SuppressionsSucessResponsetBody
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
    api_instance = API_TurboSMTP.SuppressionsApi(api_client)
    suppression_filter_order_page_request_body = API_TurboSMTP.SuppressionFilterOrderPageRequestBody() # SuppressionFilterOrderPageRequestBody | 

    try:
        # Filter suppressions
        api_response = api_instance.filter_suppressions(suppression_filter_order_page_request_body)
        print("The response of SuppressionsApi->filter_suppressions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionsApi->filter_suppressions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suppression_filter_order_page_request_body** | [**SuppressionFilterOrderPageRequestBody**](SuppressionFilterOrderPageRequestBody.md)|  | 

### Return type

[**SuppressionsSucessResponsetBody**](SuppressionsSucessResponsetBody.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sucess  Get Filtered Suppressions Data.  |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_suppressions**
> SuppressionsSucessResponsetBody get_suppressions(var_from, to, page=page, limit=limit, tz=tz, filter=filter, filter_by=filter_by, smart_search=smart_search, orderby=orderby, ordertype=ordertype)

Get Suppressions Data

Get Suppressions Data 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.list[suppression_source] import List[SuppressionSource]
from API_TurboSMTP.models.order_type import OrderType
from API_TurboSMTP.models.suppression_order_by import SuppressionOrderBy
from API_TurboSMTP.models.suppressions_sucess_responset_body import SuppressionsSucessResponsetBody
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
    api_instance = API_TurboSMTP.SuppressionsApi(api_client)
    var_from = '2020-01-01' # date | Start date
    to = '2025-12-31' # date | End date
    page = 1 # int | Page number (optional) (default to 1)
    limit = 10 # int | The numbers of rows per page to return (optional) (default to 10)
    tz = '-07:00' # str | Timezone Offset (optional)
    filter = 'Jhon.Doe@gmail.com' # str | Text to search (recipient, sender, email subject or reason for suppression) (optional)
    filter_by = API_TurboSMTP.SuppressionSource() # List[SuppressionSource] |  (optional)
    smart_search = False # bool | Smart search (optional) (default to False)
    orderby = API_TurboSMTP.SuppressionOrderBy() # SuppressionOrderBy |  (optional)
    ordertype = API_TurboSMTP.OrderType() # OrderType |  (optional)

    try:
        # Get Suppressions Data
        api_response = api_instance.get_suppressions(var_from, to, page=page, limit=limit, tz=tz, filter=filter, filter_by=filter_by, smart_search=smart_search, orderby=orderby, ordertype=ordertype)
        print("The response of SuppressionsApi->get_suppressions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionsApi->get_suppressions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **date**| Start date | 
 **to** | **date**| End date | 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| The numbers of rows per page to return | [optional] [default to 10]
 **tz** | **str**| Timezone Offset | [optional] 
 **filter** | **str**| Text to search (recipient, sender, email subject or reason for suppression) | [optional] 
 **filter_by** | [**List[SuppressionSource]**](SuppressionSource.md)|  | [optional] 
 **smart_search** | **bool**| Smart search | [optional] [default to False]
 **orderby** | [**SuppressionOrderBy**](.md)|  | [optional] 
 **ordertype** | [**OrderType**](.md)|  | [optional] 

### Return type

[**SuppressionsSucessResponsetBody**](SuppressionsSucessResponsetBody.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sucess  Get Filtered Suppressions Data.  |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_suppressions**
> SuppressionUploadResponse import_suppressions(suppression_import_json)

Import Suppressions

 Import Suppressions 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.suppression_import_json import SuppressionImportJson
from API_TurboSMTP.models.suppression_upload_response import SuppressionUploadResponse
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
    api_instance = API_TurboSMTP.SuppressionsApi(api_client)
    suppression_import_json = API_TurboSMTP.SuppressionImportJson() # SuppressionImportJson | 

    try:
        # Import Suppressions
        api_response = api_instance.import_suppressions(suppression_import_json)
        print("The response of SuppressionsApi->import_suppressions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionsApi->import_suppressions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suppression_import_json** | [**SuppressionImportJson**](SuppressionImportJson.md)|  | 

### Return type

[**SuppressionUploadResponse**](SuppressionUploadResponse.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sucess  Email Addresses were imported.  |  -  |
**400** | Bad Request  ###### Produces:  * missing_upload_file * invalid_mail_address_list  |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

