# API_TurboSMTP.AuthenticationApi

All URIs are relative to *https://pro.api.serversmtp.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authentication_login**](AuthenticationApi.md#authentication_login) | **POST** /authorize | Login - Get API Key
[**authentication_logout**](AuthenticationApi.md#authentication_logout) | **POST** /deauthorize | Logout - Revoke API Key
[**change_password**](AuthenticationApi.md#change_password) | **PUT** /change-password | Change turboSMTP password
[**check_validity_token_reset_password**](AuthenticationApi.md#check_validity_token_reset_password) | **GET** /forgot-password | Forgot Password - Verify if Secret Passord Recovery token is valid.
[**send_secret_token_reset_password**](AuthenticationApi.md#send_secret_token_reset_password) | **POST** /forgot-password | Forgot Password - Use in case you don´t remember your turboSMTP password
[**update_reset_password**](AuthenticationApi.md#update_reset_password) | **PUT** /forgot-password | Forgot Password - change password


# **authentication_login**
> AuthenticationLoginSucessResponsetBody authentication_login(authentication_login_request_body)

Login - Get API Key

**This endpoint allows you to get an API Key**  By providing your turboSMTP authentication details you will be able to get an API Key.  Use your API Key to consume APIs that require authorization. 

### Example


```python
import API_TurboSMTP
from API_TurboSMTP.models.authentication_login_request_body import AuthenticationLoginRequestBody
from API_TurboSMTP.models.authentication_login_sucess_responset_body import AuthenticationLoginSucessResponsetBody
from API_TurboSMTP.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://pro.api.serversmtp.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = API_TurboSMTP.Configuration(
    host = "https://pro.api.serversmtp.com/api/v2"
)


# Enter a context with an instance of the API client
with API_TurboSMTP.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = API_TurboSMTP.AuthenticationApi(api_client)
    authentication_login_request_body = API_TurboSMTP.AuthenticationLoginRequestBody() # AuthenticationLoginRequestBody | 

    try:
        # Login - Get API Key
        api_response = api_instance.authentication_login(authentication_login_request_body)
        print("The response of AuthenticationApi->authentication_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->authentication_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authentication_login_request_body** | [**AuthenticationLoginRequestBody**](AuthenticationLoginRequestBody.md)|  | 

### Return type

[**AuthenticationLoginSucessResponsetBody**](AuthenticationLoginSucessResponsetBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sucess  User logged in sucessfully, use the auth value as API Key from request body in future API calls.  |  -  |
**400** | Bad Request  ###### Produces:  * missing_required_parameter  |  -  |
**403** | Forbidden  Email address or password provided are incorrect.  ###### Produces:   * wrong_credentials_specified  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_logout**
> CommonMessageResponseBody authentication_logout()

Logout - Revoke API Key

**This endpoint allows you to revoke your API Key** 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.common_message_response_body import CommonMessageResponseBody
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
    api_instance = API_TurboSMTP.AuthenticationApi(api_client)

    try:
        # Logout - Revoke API Key
        api_response = api_instance.authentication_logout()
        print("The response of AuthenticationApi->authentication_logout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->authentication_logout: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CommonMessageResponseBody**](CommonMessageResponseBody.md)

### Authorization

[consumerSecret](../README.md#consumerSecret), [ApiKeyAuth](../README.md#ApiKeyAuth), [consumerKey](../README.md#consumerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sucess  User logged out sucessfully, API Key is no longer valid.  |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_password**
> CommonSuccessResponseBody change_password(change_password_request_body)

Change turboSMTP password

**This endpoint allows you to change your current password**  ## PASSWORD RULES    * Passwords must have at least 10 characters.   * At least one character must be uppercase.   * At least one character must be lowercase.   * At least one character must be numeric. 

### Example

* Api Key Authentication (consumerSecret):
* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (consumerKey):

```python
import API_TurboSMTP
from API_TurboSMTP.models.change_password_request_body import ChangePasswordRequestBody
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
    api_instance = API_TurboSMTP.AuthenticationApi(api_client)
    change_password_request_body = API_TurboSMTP.ChangePasswordRequestBody() # ChangePasswordRequestBody | 

    try:
        # Change turboSMTP password
        api_response = api_instance.change_password(change_password_request_body)
        print("The response of AuthenticationApi->change_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->change_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_password_request_body** | [**ChangePasswordRequestBody**](ChangePasswordRequestBody.md)|  | 

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
**200** | Sucess  Password changed sucessfully.     |  -  |
**400** | Bad Request  ###### Produces:  * invalid_mail_address * current_password_is_missing * current_password_can_not_be_empty * password_is_missing * password_length_should_not_be_less_than_10_characters * password_should_contain_at_least_one_uppercase_character * password_should_contain_at_least_one_lowercase_character * password_should_contain_at_least_one_digit * confirm_password_is_missing * password_should_equal_confirm_password * new_password_should_not_equal_current_password              |  -  |
**401** | Unauthorized  This API requires a valid API Key to be provided. (Use [/authentication/authorize](#/authentication/AuthenticationLogin) to obtain an API Key)  Produces:  * missing_authorization_key * invalid_authorization_key * account_is_inactive  |  -  |
**403** | Forbidden  Current password provided is incorrect.  ###### Produces:   * password_is_invalid * not_allowed_for_apikey  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_validity_token_reset_password**
> CommonSuccessResponseBody check_validity_token_reset_password(token)

Forgot Password - Verify if Secret Passord Recovery token is valid.

Forgot Password - check if secret token is valid  **Note**: Tokens are valid for 1 hour. 

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
    api_instance = API_TurboSMTP.AuthenticationApi(api_client)
    token = 'token_example' # str | Secret Token

    try:
        # Forgot Password - Verify if Secret Passord Recovery token is valid.
        api_response = api_instance.check_validity_token_reset_password(token)
        print("The response of AuthenticationApi->check_validity_token_reset_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->check_validity_token_reset_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Secret Token | 

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
**200** | Sucess  Token is valid.    |  -  |
**400** | Bad Request  ###### Produces:  * forgot_password_token_is_missing  |  -  |
**403** | Forbidden  Token is invalid.    |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_secret_token_reset_password**
> CommonSuccessResponseBody send_secret_token_reset_password(send_secret_token_reset_password_request_body)

Forgot Password - Use in case you don´t remember your turboSMTP password

**This endpoint will allow you to get an email that will help you reset your turboSMTP password**  In your password reset email you will find:  * A **Reset Password** button that will take you to the password reset form on turboSMTP website. * A secret token to be used to reset the password via [/authentication/forgot-password](#/authentication/updateResetPassword). **Note**: Token is vaid for 1 hour. 

### Example


```python
import API_TurboSMTP
from API_TurboSMTP.models.common_success_response_body import CommonSuccessResponseBody
from API_TurboSMTP.models.send_secret_token_reset_password_request_body import SendSecretTokenResetPasswordRequestBody
from API_TurboSMTP.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://pro.api.serversmtp.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = API_TurboSMTP.Configuration(
    host = "https://pro.api.serversmtp.com/api/v2"
)


# Enter a context with an instance of the API client
with API_TurboSMTP.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = API_TurboSMTP.AuthenticationApi(api_client)
    send_secret_token_reset_password_request_body = API_TurboSMTP.SendSecretTokenResetPasswordRequestBody() # SendSecretTokenResetPasswordRequestBody | 

    try:
        # Forgot Password - Use in case you don´t remember your turboSMTP password
        api_response = api_instance.send_secret_token_reset_password(send_secret_token_reset_password_request_body)
        print("The response of AuthenticationApi->send_secret_token_reset_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->send_secret_token_reset_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_secret_token_reset_password_request_body** | [**SendSecretTokenResetPasswordRequestBody**](SendSecretTokenResetPasswordRequestBody.md)|  | 

### Return type

[**CommonSuccessResponseBody**](CommonSuccessResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sucess  Password reset email with instructions was sent to your turboSMTP email account.     |  -  |
**400** | Bad Request  ###### Produces:  * empty_request_body * missing_required_parameter     |  -  |
**404** | Not Found  Please verify the email address provided is the one you used to register at turboSMTP.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_reset_password**
> CommonSuccessResponseBody update_reset_password(update_reset_password_request_body)

Forgot Password - change password

**This endpoint allows you to reset your password by using a password reset token**  ## PASSWORD RULES    * Passwords must have at least 10 characters.   * At least one character must be uppercase.   * At least one character must be lowercase.   * At least one character must be numeric. 

### Example


```python
import API_TurboSMTP
from API_TurboSMTP.models.common_success_response_body import CommonSuccessResponseBody
from API_TurboSMTP.models.update_reset_password_request_body import UpdateResetPasswordRequestBody
from API_TurboSMTP.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://pro.api.serversmtp.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = API_TurboSMTP.Configuration(
    host = "https://pro.api.serversmtp.com/api/v2"
)


# Enter a context with an instance of the API client
with API_TurboSMTP.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = API_TurboSMTP.AuthenticationApi(api_client)
    update_reset_password_request_body = API_TurboSMTP.UpdateResetPasswordRequestBody() # UpdateResetPasswordRequestBody | 

    try:
        # Forgot Password - change password
        api_response = api_instance.update_reset_password(update_reset_password_request_body)
        print("The response of AuthenticationApi->update_reset_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->update_reset_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_reset_password_request_body** | [**UpdateResetPasswordRequestBody**](UpdateResetPasswordRequestBody.md)|  | 

### Return type

[**CommonSuccessResponseBody**](CommonSuccessResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sucess  Password reset sucessfully.     |  -  |
**400** | Bad Request  ###### Produces:  * empty_request_body * token_is_missing * token_can_not_be_empty * password_is_missing * password_length_should_not_be_less_than_10_characters * password_should_contain_at_least_one_uppercase_character * password_should_contain_at_least_one_lowercase_character * password_should_contain_at_least_one_digit * confirm_password_is_missing * password_should_equal_confirm_password  |  -  |
**403** | Forbidden  Token is invalid.    |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

