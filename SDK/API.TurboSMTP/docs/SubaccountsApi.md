# API_TurboSMTP.SubaccountsApi

All URIs are relative to *https://pro.api.serversmtp.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_if_account_email_exists**](SubaccountsApi.md#check_if_account_email_exists) | **GET** /subaccounts/email-exists | Check if account email exists in turboSMTP
[**create_subaccount**](SubaccountsApi.md#create_subaccount) | **POST** /subaccounts | Create Subaccount.
[**delete_logo_file**](SubaccountsApi.md#delete_logo_file) | **DELETE** /subaccounts/logo | Delete agency logo
[**get_active_plan**](SubaccountsApi.md#get_active_plan) | **GET** /subaccounts/{Id}/active-plan | Get subaccount active plan.
[**get_agency_settings**](SubaccountsApi.md#get_agency_settings) | **GET** /subaccounts/agency | Update Agency details
[**get_logo_file**](SubaccountsApi.md#get_logo_file) | **GET** /subaccounts/logo | Get agency logo
[**get_subaccount_details**](SubaccountsApi.md#get_subaccount_details) | **GET** /subaccounts/{Id} | Get sub account details
[**get_subaccounts**](SubaccountsApi.md#get_subaccounts) | **GET** /subaccounts/list | Get Subaccounts lists information
[**subaccount_authentication_login**](SubaccountsApi.md#subaccount_authentication_login) | **POST** /subaccounts/authorize | Login to a subaccount
[**update_agency_settings**](SubaccountsApi.md#update_agency_settings) | **PATCH** /subaccounts/agency | Update Agency details
[**update_subaccount_details**](SubaccountsApi.md#update_subaccount_details) | **PATCH** /subaccounts/{Id} | Update sub account details
[**update_subaccount_smtp_limit**](SubaccountsApi.md#update_subaccount_smtp_limit) | **POST** /subaccounts/{Id}/updatesubaccountsmtplimit | Set subaccount smtp limit
[**update_subaccount_status**](SubaccountsApi.md#update_subaccount_status) | **POST** /subaccounts/{Id}/updatesubaccountstatus | Set subaccount status
[**upload_logo_file**](SubaccountsApi.md#upload_logo_file) | **POST** /subaccounts/logo | Upload agency logo


# **check_if_account_email_exists**
> CommmonResultResponseBody check_if_account_email_exists(email)

Check if account email exists in turboSMTP

 Check if account email exists in turboSMTP 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.commmon_result_response_body import CommmonResultResponseBody
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
    api_instance = API_TurboSMTP.SubaccountsApi(api_client)
    email = 'username@gmail.com' # str | Email address.

    try:
        # Check if account email exists in turboSMTP
        api_response = api_instance.check_if_account_email_exists(email)
        print("The response of SubaccountsApi->check_if_account_email_exists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubaccountsApi->check_if_account_email_exists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email address. | 

### Return type

[**CommmonResultResponseBody**](CommmonResultResponseBody.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sucess  Returns true if email address is already associated to a turboSMTP account.   |  -  |
**400** | Bad Request  ###### Produces:  * missing_required_parameter_email  |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |
**403** | Forbidden  The current active plan does not include this feature, upgrade is required to use this feature.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subaccount**
> Subaccount create_subaccount(subaccount_create_request)

Create Subaccount.

 Create subaccount. 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.subaccount import Subaccount
from API_TurboSMTP.models.subaccount_create_request import SubaccountCreateRequest
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
    api_instance = API_TurboSMTP.SubaccountsApi(api_client)
    subaccount_create_request = API_TurboSMTP.SubaccountCreateRequest() # SubaccountCreateRequest | 

    try:
        # Create Subaccount.
        api_response = api_instance.create_subaccount(subaccount_create_request)
        print("The response of SubaccountsApi->create_subaccount:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubaccountsApi->create_subaccount: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subaccount_create_request** | [**SubaccountCreateRequest**](SubaccountCreateRequest.md)|  | 

### Return type

[**Subaccount**](Subaccount.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Sub account details. |  -  |
**400** | Bad Request  ###### Produces:  * email_is_already_in_use * missing_required_parameter_email * missing_required_parameter_first_name * missing_required_parameter_last_name * missing_required_parameter_password * password_length_should_not_be_less_than_10_characters * password_should_contain_at_least_one_uppercase_character * password_should_contain_at_least_one_digit * missing_required_parameter_confirm_password * password_should_equal_confirm_password * missing_required_parameter_ip * ip_should_be_IPV4_format * ip_not_associated_to_user_account * policy_agree_should_be_true  |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |
**403** | Forbidden  The current active plan does not include this feature, upgrade is required to use this feature.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_logo_file**
> CommonSuccessResponseBody delete_logo_file()

Delete agency logo

 Delete agency logo 

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
    api_instance = API_TurboSMTP.SubaccountsApi(api_client)

    try:
        # Delete agency logo
        api_response = api_instance.delete_logo_file()
        print("The response of SubaccountsApi->delete_logo_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubaccountsApi->delete_logo_file: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | Sucess  Logo was deleted.  |  -  |
**404** | Not Found  Agency Logo was not found.  |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_plan**
> SubaccountActivePlan get_active_plan(id)

Get subaccount active plan.

 Get subaccount active plan. 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.subaccount_active_plan import SubaccountActivePlan
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
    api_instance = API_TurboSMTP.SubaccountsApi(api_client)
    id = 56 # int | Id

    try:
        # Get subaccount active plan.
        api_response = api_instance.get_active_plan(id)
        print("The response of SubaccountsApi->get_active_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubaccountsApi->get_active_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id | 

### Return type

[**SubaccountActivePlan**](SubaccountActivePlan.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Login successfull |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |
**403** | Forbidden  The current active plan does not include this feature, upgrade is required to use this feature.  |  -  |
**404** | Not Found  Please verify the subaccount id is valid.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agency_settings**
> AgencySettings get_agency_settings()

Update Agency details

 Get Agency details. 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.agency_settings import AgencySettings
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
    api_instance = API_TurboSMTP.SubaccountsApi(api_client)

    try:
        # Update Agency details
        api_response = api_instance.get_agency_settings()
        print("The response of SubaccountsApi->get_agency_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubaccountsApi->get_agency_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AgencySettings**](AgencySettings.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agency details. |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logo_file**
> Logo get_logo_file()

Get agency logo

 Get agency logo 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.logo import Logo
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
    api_instance = API_TurboSMTP.SubaccountsApi(api_client)

    try:
        # Get agency logo
        api_response = api_instance.get_logo_file()
        print("The response of SubaccountsApi->get_logo_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubaccountsApi->get_logo_file: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Logo**](Logo.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agency Logo Url  |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subaccount_details**
> Subaccount get_subaccount_details(id)

Get sub account details

 Get sub account details. 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.subaccount import Subaccount
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
    api_instance = API_TurboSMTP.SubaccountsApi(api_client)
    id = 56 # int | Id

    try:
        # Get sub account details
        api_response = api_instance.get_subaccount_details(id)
        print("The response of SubaccountsApi->get_subaccount_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubaccountsApi->get_subaccount_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id | 

### Return type

[**Subaccount**](Subaccount.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sub account details. |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |
**403** | Forbidden  The current active plan does not include this feature, upgrade is required to use this feature.  |  -  |
**404** | Not Found  Please verify the subaccount id is valid.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subaccounts**
> SubAccountListSucessResponsetBody get_subaccounts(page=page, limit=limit, filter_by_email=filter_by_email, filter_by_active=filter_by_active, filter_by_ip=filter_by_ip, orderby=orderby, ordertype=ordertype)

Get Subaccounts lists information

 List subaccounts information 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.order_type import OrderType
from API_TurboSMTP.models.sub_account_list_sucess_responset_body import SubAccountListSucessResponsetBody
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
    api_instance = API_TurboSMTP.SubaccountsApi(api_client)
    page = 1 # int | Page number (optional) (default to 1)
    limit = 10 # int | The numbers of rows per page to return (optional) (default to 10)
    filter_by_email = 'Jhon' # str | Filter by email addresses that fully/partially match the search value. (optional)
    filter_by_active = true # bool | Filter by subaccount status. (optional)
    filter_by_ip = ['filter_by_ip_example'] # List[str] | Filter by IP Addresses. (optional)
    orderby = 'email' # str | Field to sort by (optional) (default to 'email')
    ordertype = API_TurboSMTP.OrderType() # OrderType |  (optional)

    try:
        # Get Subaccounts lists information
        api_response = api_instance.get_subaccounts(page=page, limit=limit, filter_by_email=filter_by_email, filter_by_active=filter_by_active, filter_by_ip=filter_by_ip, orderby=orderby, ordertype=ordertype)
        print("The response of SubaccountsApi->get_subaccounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubaccountsApi->get_subaccounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| The numbers of rows per page to return | [optional] [default to 10]
 **filter_by_email** | **str**| Filter by email addresses that fully/partially match the search value. | [optional] 
 **filter_by_active** | **bool**| Filter by subaccount status. | [optional] 
 **filter_by_ip** | [**List[str]**](str.md)| Filter by IP Addresses. | [optional] 
 **orderby** | **str**| Field to sort by | [optional] [default to &#39;email&#39;]
 **ordertype** | [**OrderType**](.md)|  | [optional] 

### Return type

[**SubAccountListSucessResponsetBody**](SubAccountListSucessResponsetBody.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sucess  Subaccounts list.  |  -  |
**400** | Bad Request  ###### Produces:  * page_should_be_integer * page_should_be_greater_than_0 * limit_should_be_integer * limit_should_be_greater_than_0 * filter_by_active_should_be_boolean * ip_should_be_IPV4_format * order_by_can_only_be_email_or_last_used * ordertype_should_be_asc_or_desc  |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |
**403** | Forbidden  The current active plan does not include this feature, upgrade is required to use this feature.  |  -  |
**404** | Not Found  Page not found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subaccount_authentication_login**
> AuthenticationLoginSucessResponsetBody subaccount_authentication_login(email1)

Login to a subaccount

 Login to a subaccount. 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.authentication_login_sucess_responset_body import AuthenticationLoginSucessResponsetBody
from API_TurboSMTP.models.email1 import Email1
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
    api_instance = API_TurboSMTP.SubaccountsApi(api_client)
    email1 = API_TurboSMTP.Email1() # Email1 | 

    try:
        # Login to a subaccount
        api_response = api_instance.subaccount_authentication_login(email1)
        print("The response of SubaccountsApi->subaccount_authentication_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubaccountsApi->subaccount_authentication_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email1** | [**Email1**](Email1.md)|  | 

### Return type

[**AuthenticationLoginSucessResponsetBody**](AuthenticationLoginSucessResponsetBody.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sucess  User logged in sucessfully, use the auth value as API Key from request body in future API calls.  |  -  |
**400** | Bad Request  ###### Produces:  * missing_required_parameter_email  |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |
**403** | Forbidden  Email address or password provided are incorrect.  ###### Produces:   * wrong_credentials_specified * feature_not_available_for_active_plan  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agency_settings**
> CommonSuccessResponseBody update_agency_settings(base_agency_settings)

Update Agency details

 Update Agency Details 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.base_agency_settings import BaseAgencySettings
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
    api_instance = API_TurboSMTP.SubaccountsApi(api_client)
    base_agency_settings = API_TurboSMTP.BaseAgencySettings() # BaseAgencySettings | 

    try:
        # Update Agency details
        api_response = api_instance.update_agency_settings(base_agency_settings)
        print("The response of SubaccountsApi->update_agency_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubaccountsApi->update_agency_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_agency_settings** | [**BaseAgencySettings**](BaseAgencySettings.md)|  | 

### Return type

[**CommonSuccessResponseBody**](CommonSuccessResponseBody.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sucess  Agency details updated sucessfully  |  -  |
**400** | Bad Request  ###### Produces:  * agency_name_should_be_shorter_than_128_characters * agency_website_should_be_shorter_than_128_characters * agency_footer_should_be_shorter_than_2048_characters  |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subaccount_details**
> Subaccount update_subaccount_details(id, subaccount_update_request)

Update sub account details

 Update sub account details. 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.subaccount import Subaccount
from API_TurboSMTP.models.subaccount_update_request import SubaccountUpdateRequest
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
    api_instance = API_TurboSMTP.SubaccountsApi(api_client)
    id = 56 # int | Id
    subaccount_update_request = API_TurboSMTP.SubaccountUpdateRequest() # SubaccountUpdateRequest | 

    try:
        # Update sub account details
        api_response = api_instance.update_subaccount_details(id, subaccount_update_request)
        print("The response of SubaccountsApi->update_subaccount_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubaccountsApi->update_subaccount_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id | 
 **subaccount_update_request** | [**SubaccountUpdateRequest**](SubaccountUpdateRequest.md)|  | 

### Return type

[**Subaccount**](Subaccount.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sub account updated sucessfully. |  -  |
**400** | Bad Request  ###### Produces:  * password_length_should_not_be_less_than_10_characters * password_should_contain_at_least_one_uppercase_character * password_should_contain_at_least_one_digit * password_should_equal_confirm_password * ip_should_be_IPV4_format * ip_not_associated_to_user_account * policy_agree_should_be_true  |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |
**403** | Forbidden  The current active plan does not include this feature, upgrade is required to use this feature.  |  -  |
**404** | Not Found  Please verify the subaccount id is valid.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subaccount_smtp_limit**
> SubaccountActivePlan update_subaccount_smtp_limit(id, subaccount_smtp_limit)

Set subaccount smtp limit

 Set subaccount smtp limit. 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.subaccount_active_plan import SubaccountActivePlan
from API_TurboSMTP.models.subaccount_smtp_limit import SubaccountSMTPLimit
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
    api_instance = API_TurboSMTP.SubaccountsApi(api_client)
    id = 56 # int | Id
    subaccount_smtp_limit = API_TurboSMTP.SubaccountSMTPLimit() # SubaccountSMTPLimit | 

    try:
        # Set subaccount smtp limit
        api_response = api_instance.update_subaccount_smtp_limit(id, subaccount_smtp_limit)
        print("The response of SubaccountsApi->update_subaccount_smtp_limit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubaccountsApi->update_subaccount_smtp_limit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id | 
 **subaccount_smtp_limit** | [**SubaccountSMTPLimit**](SubaccountSMTPLimit.md)|  | 

### Return type

[**SubaccountActivePlan**](SubaccountActivePlan.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subaccount smtp limit set sucessfully |  -  |
**400** | Bad Request  ###### Produces:  * missing_required_parameter_limit * limit_should_be_integer * limit_should_not_be_higher_than_parent_account_limit * limit_should_not_be_lower_than_-1  |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |
**403** | Forbidden  The current active plan does not include this feature, upgrade is required to use this feature.  |  -  |
**404** | Not Found  Please verify the subaccount id is valid.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subaccount_status**
> SubaccountActivePlan update_subaccount_status(id, subaccount_active_status)

Set subaccount status

 Set subaccount status. 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.subaccount_active_plan import SubaccountActivePlan
from API_TurboSMTP.models.subaccount_active_status import SubaccountActiveStatus
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
    api_instance = API_TurboSMTP.SubaccountsApi(api_client)
    id = 56 # int | Id
    subaccount_active_status = API_TurboSMTP.SubaccountActiveStatus() # SubaccountActiveStatus | 

    try:
        # Set subaccount status
        api_response = api_instance.update_subaccount_status(id, subaccount_active_status)
        print("The response of SubaccountsApi->update_subaccount_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubaccountsApi->update_subaccount_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id | 
 **subaccount_active_status** | [**SubaccountActiveStatus**](SubaccountActiveStatus.md)|  | 

### Return type

[**SubaccountActivePlan**](SubaccountActivePlan.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subaccount status set sucessfully |  -  |
**400** | Bad Request  ###### Produces:  * missing_required_parameter_active * active_should_be_boolean   |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |
**403** | Forbidden  The current active plan does not include this feature, upgrade is required to use this feature.  |  -  |
**404** | Not Found  Please verify the subaccount id is valid.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_logo_file**
> CommonSuccessResponseBody upload_logo_file(file=file)

Upload agency logo

 Upload agency logo.  Logo must be a png or jpeg image. 

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
    api_instance = API_TurboSMTP.SubaccountsApi(api_client)
    file = None # bytearray |  (optional)

    try:
        # Upload agency logo
        api_response = api_instance.upload_logo_file(file=file)
        print("The response of SubaccountsApi->upload_logo_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubaccountsApi->upload_logo_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | [optional] 

### Return type

[**CommonSuccessResponseBody**](CommonSuccessResponseBody.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sucess  The Logo file was successfully submitted.  |  -  |
**400** | Bad Request  ###### Produces:  * missing_upload_file * file_type_should_be_png_or_jpeg  |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

