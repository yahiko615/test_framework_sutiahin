from http import HTTPStatus

from api_collections.ping_api import PingAPI
HTTP_CODE_CREATED_ERROR = f'Status code is different form expected. Expected: {HTTPStatus.CREATED}'
import allure


def test_ping(env):
    ping_api = PingAPI(env)
    response = ping_api.ping()
    assert response.status_code == HTTPStatus.CREATED, HTTP_CODE_CREATED_ERROR
