import json
from http import HTTPStatus

from api_collections.booking_api import BookingAPI
from api_collections.data_classes.booking_data import Booking

HTTP_CODE_OK_ERROR = f'Status code is different form expected. Expected: {HTTPStatus.OK}'
HTTP_CODE_CREATED_ERROR = f'Status code is different form expected. Expected: {HTTPStatus.CREATED}'
HTTP_CODE_NOT_FOUND_ERROR = f'Status code is different form expected. Expected: {HTTPStatus.NOT_FOUND}'


def test_status_code_200(env, create_mock_booking):
    booking_api = BookingAPI(env)
    response = booking_api.get_booking_by_id(booking_id=1)
    data = json.loads(response.text)
    assert response.status_code == HTTPStatus.OK, HTTP_CODE_OK_ERROR
    actual_booking = Booking(**data)
    assert create_mock_booking.get_dict_without_id() == actual_booking.get_dict_without_id()


def test_get_ids(env):
    booking_api = BookingAPI(env)
    response = booking_api.get_booking()
    assert response.status_code == HTTPStatus.OK, HTTP_CODE_OK_ERROR
    assert 'bookingid' in response.json()[0], 'Bookingid is missing'


def test_create_booking(env, create_mock_booking_with_id):
    booking_api = BookingAPI(env)
    response = booking_api.create_booking(create_mock_booking_with_id)
    assert response.status_code == HTTPStatus.OK
    get_created_booking = booking_api.get_booking_by_response(response)
    created_booking = json.loads(get_created_booking.text)
    assert get_created_booking.status_code == HTTPStatus.OK, HTTP_CODE_OK_ERROR
    assert created_booking == create_mock_booking_with_id.get_dict_without_id(), ''


def test_update_booking(create_mock_booking_with_id, env):
    booking_api = BookingAPI(env)
    booking_api.setup_token(env)
    booking_to_update = create_mock_booking_with_id
    id_to_update = booking_to_update.bookingid
    booking_to_update.firstname = 'Misha'
    booking_to_update.totalprice = 1052
    response = booking_api.put_booking(id_to_update, booking_to_update)
    assert response.status_code == HTTPStatus.OK, HTTP_CODE_OK_ERROR
    updated_booking = Booking(**response.json())
    assert updated_booking.firstname == booking_to_update.firstname, 'Booking update error. Param firstname differents'
    assert updated_booking.totalprice == booking_to_update.totalprice, \
        'Booking update error. Param totalprice differents'


def test_patch_booking(env, create_mock_booking_with_id):
    booking_api = BookingAPI(env)
    booking_api.setup_token(env)
    id_to_patch = create_mock_booking_with_id.bookingid
    patch_dict = {"firstname": "Misha", "totalprice": 1052}
    response = booking_api.patch_booking(id_to_patch, patch_dict)
    assert response.status_code == HTTPStatus.OK, HTTP_CODE_OK_ERROR
    patched_booking = Booking(**response.json())
    assert patched_booking.firstname == patch_dict['firstname'], 'Booking patch error. Param firstname differents'
    assert patched_booking.totalprice == patch_dict[
        'totalprice'], 'Booking patch error. Param totalprice differents'


def test_delete_booking(env, create_mock_booking_with_id):
    booking_api = BookingAPI(env)
    booking_api.setup_token(env)
    id_to_delete = create_mock_booking_with_id.bookingid
    delete_response = booking_api.delete_booking(id_to_delete)
    assert delete_response.status_code == HTTPStatus.CREATED, HTTP_CODE_CREATED_ERROR
    result_after_delete = booking_api.get_booking_by_id(id_to_delete)
    assert result_after_delete.status_code == HTTPStatus.NOT_FOUND, HTTP_CODE_NOT_FOUND_ERROR


def test_get_non_existent_booking(env, create_mock_booking):
    booking_api = BookingAPI(env)
    response = booking_api.get_booking_by_id(booking_id='qew')
    assert response.status_code == HTTPStatus.NOT_FOUND, HTTP_CODE_NOT_FOUND_ERROR
