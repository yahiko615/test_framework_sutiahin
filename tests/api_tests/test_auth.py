from http import HTTPStatus

from api_collections.auth_api import AuthAPI
HTTP_CODE_OK_ERROR = f'Status code is different form expected. Expected: {HTTPStatus.OK}'
import allure


@allure.feature('Api auth')
def test_creating_token(env):
    auth_api = AuthAPI(env)
    response = auth_api.create_token()
    assert response.status_code == HTTPStatus.OK, HTTP_CODE_OK_ERROR
    assert 'token' in response.json()


@allure.feature('Api auth')
def test_creating_token_with_invalid_creds(env):
    invalid_password = 'dasda123414'
    invalid_login = 'admidn'
    invalid_creds = {"username": f"{invalid_password}", "password": f"{invalid_login}"}
    auth_api = AuthAPI(env)
    response = auth_api.create_token(invalid_creds)
    assert response.status_code == HTTPStatus.OK, HTTP_CODE_OK_ERROR
    assert response.json()['reason'] == "Bad credentials", "Token created with bad arguments or missing"
