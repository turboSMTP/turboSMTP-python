# API_TurboSMTP.AnalyticsApi

All URIs are relative to *https://pro.api.serversmtp.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_analytics_data_csv**](AnalyticsApi.md#export_analytics_data_csv) | **GET** /analytics/csv | Export Analytics data in CSV file
[**get_analytics_data**](AnalyticsApi.md#get_analytics_data) | **GET** /analytics | Get Analytics Data
[**get_analytics_data_by_id**](AnalyticsApi.md#get_analytics_data_by_id) | **GET** /analytics/{Id} | Get Analytics Single Item by ID


# **export_analytics_data_csv**
> str export_analytics_data_csv(var_from, to, status=status, filter_by=filter_by, filter=filter, smart_search=smart_search, orderby=orderby, ordertype=ordertype, tz=tz)

Export Analytics data in CSV file

Export Analytics data in CSV file 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.analytic_mail_status import AnalyticMailStatus
from API_TurboSMTP.models.analytic_order_by import AnalyticOrderBy
from API_TurboSMTP.models.list[analytic_filter_by_option] import List[AnalyticFilterByOption]
from API_TurboSMTP.models.order_type import OrderType
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
    api_instance = API_TurboSMTP.AnalyticsApi(api_client)
    var_from = '2020-01-01' # date | Start date
    to = '2025-12-31' # date | End date
    status = [API_TurboSMTP.AnalyticMailStatus()] # List[AnalyticMailStatus] | Filter by Status      NEW: email has been queued for delivery     DEFER: email is in the queue for delivery     SUCCESS: email has been delivered.     OPEN: email has been opened.     CLICK: email has been clicked.     REPORT: email has been reported as spam.     FAIL: email has bounced.     SYSFAIL: email was dropped.     UNSUB: email is unsubscribed.  <br /> Notice that emails that fall into the above statuses can be grouped, ie Turbo-Smtp uses the following groups: <br />      'Clicks' = 'CLICK',     'Unsubscribes' = 'UNSUB',     'Spam' = 'REPORT',     'Drop' = 'SYSFAIL',     'Queued' = 'NEW' or 'DEFER',     'Opens'= 'OPEN' or 'CLICK' or 'UNSUB' or 'REPORT',     'Delivered'= 'SUCCESS'  or 'OPEN' or 'CLICK' or 'UNSUB' or 'REPORT',     'Bounce': 'FAIL'.    (optional)
    filter_by = API_TurboSMTP.AnalyticFilterByOption() # List[AnalyticFilterByOption] | Filter by (optional)
    filter = 'September 2022' # str | Text to search (recipient, sender, email subject or reason for suppression) (optional)
    smart_search = False # bool | Smart search (optional) (default to False)
    orderby = API_TurboSMTP.AnalyticOrderBy() # AnalyticOrderBy | Order by (optional)
    ordertype = API_TurboSMTP.OrderType() # OrderType |  (optional)
    tz = '-07:00' # str | Timezone Offset (optional)

    try:
        # Export Analytics data in CSV file
        api_response = api_instance.export_analytics_data_csv(var_from, to, status=status, filter_by=filter_by, filter=filter, smart_search=smart_search, orderby=orderby, ordertype=ordertype, tz=tz)
        print("The response of AnalyticsApi->export_analytics_data_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->export_analytics_data_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **date**| Start date | 
 **to** | **date**| End date | 
 **status** | [**List[AnalyticMailStatus]**](AnalyticMailStatus.md)| Filter by Status      NEW: email has been queued for delivery     DEFER: email is in the queue for delivery     SUCCESS: email has been delivered.     OPEN: email has been opened.     CLICK: email has been clicked.     REPORT: email has been reported as spam.     FAIL: email has bounced.     SYSFAIL: email was dropped.     UNSUB: email is unsubscribed.  &lt;br /&gt; Notice that emails that fall into the above statuses can be grouped, ie Turbo-Smtp uses the following groups: &lt;br /&gt;      &#39;Clicks&#39; &#x3D; &#39;CLICK&#39;,     &#39;Unsubscribes&#39; &#x3D; &#39;UNSUB&#39;,     &#39;Spam&#39; &#x3D; &#39;REPORT&#39;,     &#39;Drop&#39; &#x3D; &#39;SYSFAIL&#39;,     &#39;Queued&#39; &#x3D; &#39;NEW&#39; or &#39;DEFER&#39;,     &#39;Opens&#39;&#x3D; &#39;OPEN&#39; or &#39;CLICK&#39; or &#39;UNSUB&#39; or &#39;REPORT&#39;,     &#39;Delivered&#39;&#x3D; &#39;SUCCESS&#39;  or &#39;OPEN&#39; or &#39;CLICK&#39; or &#39;UNSUB&#39; or &#39;REPORT&#39;,     &#39;Bounce&#39;: &#39;FAIL&#39;.    | [optional] 
 **filter_by** | [**List[AnalyticFilterByOption]**](AnalyticFilterByOption.md)| Filter by | [optional] 
 **filter** | **str**| Text to search (recipient, sender, email subject or reason for suppression) | [optional] 
 **smart_search** | **bool**| Smart search | [optional] [default to False]
 **orderby** | [**AnalyticOrderBy**](.md)| Order by | [optional] 
 **ordertype** | [**OrderType**](.md)|  | [optional] 
 **tz** | **str**| Timezone Offset | [optional] 

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
**200** | Analytics CSV data |  -  |
**400** | Bad Request  ###### Produces:  * missing_required_parameter_from * from_format_should_be_yyyy-mm-dd * missing_required_parameter_to * to_format_should_be_yyyy-mm-dd * missing_required_parameter_filter_by * invalid_status_value * filter_by_can_only_be_subject_or_sender_or_recipient_or_domain * smart_search_should_be_true_or_false * orderby_can_only_be_subject_or_sender_or_recipient_or_domain * ordertype_should_be_asc_or_desc                    |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analytics_data**
> AnalyticsListSucessResponsetBody get_analytics_data(var_from, to, page=page, limit=limit, status=status, filter_by=filter_by, filter=filter, smart_search=smart_search, orderby=orderby, ordertype=ordertype, tz=tz)

Get Analytics Data

Get Analytics Data 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.analytic_mail_status import AnalyticMailStatus
from API_TurboSMTP.models.analytic_order_by import AnalyticOrderBy
from API_TurboSMTP.models.analytics_list_sucess_responset_body import AnalyticsListSucessResponsetBody
from API_TurboSMTP.models.list[analytic_filter_by_option] import List[AnalyticFilterByOption]
from API_TurboSMTP.models.order_type import OrderType
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
    api_instance = API_TurboSMTP.AnalyticsApi(api_client)
    var_from = '2020-01-01' # date | Start date
    to = '2025-12-31' # date | End date
    page = 1 # int | Page number (optional) (default to 1)
    limit = 10 # int | The numbers of rows per page to return (optional) (default to 10)
    status = [API_TurboSMTP.AnalyticMailStatus()] # List[AnalyticMailStatus] | Filter by Status      NEW: email has been queued for delivery     DEFER: email is in the queue for delivery     SUCCESS: email has been delivered.     OPEN: email has been opened.     CLICK: email has been clicked.     REPORT: email has been reported as spam.     FAIL: email has bounced.     SYSFAIL: email was dropped.     UNSUB: email is unsubscribed.  <br /> Notice that emails that fall into the above statuses can be grouped, ie Turbo-Smtp uses the following groups: <br />      'Clicks' = 'CLICK',     'Unsubscribes' = 'UNSUB',     'Spam' = 'REPORT',     'Drop' = 'SYSFAIL',     'Queued' = 'NEW' or 'DEFER',     'Opens'= 'OPEN' or 'CLICK' or 'UNSUB' or 'REPORT',     'Delivered'= 'SUCCESS'  or 'OPEN' or 'CLICK' or 'UNSUB' or 'REPORT',     'Bounce': 'FAIL'.    (optional)
    filter_by = API_TurboSMTP.AnalyticFilterByOption() # List[AnalyticFilterByOption] | Filter by (optional)
    filter = 'September 2022' # str | Text to search (recipient, sender, email subject or reason for suppression) (optional)
    smart_search = False # bool | Smart search (optional) (default to False)
    orderby = API_TurboSMTP.AnalyticOrderBy() # AnalyticOrderBy | Order by (optional)
    ordertype = API_TurboSMTP.OrderType() # OrderType |  (optional)
    tz = '-07:00' # str | Timezone Offset (optional)

    try:
        # Get Analytics Data
        api_response = api_instance.get_analytics_data(var_from, to, page=page, limit=limit, status=status, filter_by=filter_by, filter=filter, smart_search=smart_search, orderby=orderby, ordertype=ordertype, tz=tz)
        print("The response of AnalyticsApi->get_analytics_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->get_analytics_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **date**| Start date | 
 **to** | **date**| End date | 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| The numbers of rows per page to return | [optional] [default to 10]
 **status** | [**List[AnalyticMailStatus]**](AnalyticMailStatus.md)| Filter by Status      NEW: email has been queued for delivery     DEFER: email is in the queue for delivery     SUCCESS: email has been delivered.     OPEN: email has been opened.     CLICK: email has been clicked.     REPORT: email has been reported as spam.     FAIL: email has bounced.     SYSFAIL: email was dropped.     UNSUB: email is unsubscribed.  &lt;br /&gt; Notice that emails that fall into the above statuses can be grouped, ie Turbo-Smtp uses the following groups: &lt;br /&gt;      &#39;Clicks&#39; &#x3D; &#39;CLICK&#39;,     &#39;Unsubscribes&#39; &#x3D; &#39;UNSUB&#39;,     &#39;Spam&#39; &#x3D; &#39;REPORT&#39;,     &#39;Drop&#39; &#x3D; &#39;SYSFAIL&#39;,     &#39;Queued&#39; &#x3D; &#39;NEW&#39; or &#39;DEFER&#39;,     &#39;Opens&#39;&#x3D; &#39;OPEN&#39; or &#39;CLICK&#39; or &#39;UNSUB&#39; or &#39;REPORT&#39;,     &#39;Delivered&#39;&#x3D; &#39;SUCCESS&#39;  or &#39;OPEN&#39; or &#39;CLICK&#39; or &#39;UNSUB&#39; or &#39;REPORT&#39;,     &#39;Bounce&#39;: &#39;FAIL&#39;.    | [optional] 
 **filter_by** | [**List[AnalyticFilterByOption]**](AnalyticFilterByOption.md)| Filter by | [optional] 
 **filter** | **str**| Text to search (recipient, sender, email subject or reason for suppression) | [optional] 
 **smart_search** | **bool**| Smart search | [optional] [default to False]
 **orderby** | [**AnalyticOrderBy**](.md)| Order by | [optional] 
 **ordertype** | [**OrderType**](.md)|  | [optional] 
 **tz** | **str**| Timezone Offset | [optional] 

### Return type

[**AnalyticsListSucessResponsetBody**](AnalyticsListSucessResponsetBody.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sucess  Get Analytics Data.  |  -  |
**400** | Bad Request  ###### Produces:  * page_should_be_integer * page_should_be_greater_than_0 * limit_should_be_integer * limit_should_be_greater_than_0 * missing_required_parameter_from * from_format_should_be_yyyy-mm-dd * missing_required_parameter_to * to_format_should_be_yyyy-mm-dd * missing_required_parameter_filter_by * invalid_status_value * filter_by_can_only_be_subject_or_sender_or_recipient_or_domain * smart_search_should_be_true_or_false * orderby_can_only_be_subject_or_sender_or_recipient_or_domain * ordertype_should_be_asc_or_desc                    |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analytics_data_by_id**
> AnalyticMailItem get_analytics_data_by_id(id)

Get Analytics Single Item by ID

Get Analytics Data by ID 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.analytic_mail_item import AnalyticMailItem
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
    api_instance = API_TurboSMTP.AnalyticsApi(api_client)
    id = 56 # int | Id

    try:
        # Get Analytics Single Item by ID
        api_response = api_instance.get_analytics_data_by_id(id)
        print("The response of AnalyticsApi->get_analytics_data_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->get_analytics_data_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id | 

### Return type

[**AnalyticMailItem**](AnalyticMailItem.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sucess  Response body contains the Analytic Item requested by ID.  |  -  |
**400** | Bad Request  ###### Produces:  * XXXXXXX  |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |
**404** | Not Found  The Analytic ID was not found  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

