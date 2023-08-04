import json
from api_collections.auth_api import AuthAPI
from utilities.api_utilities.base_api import BaseAPI


class BookingAPI(BaseAPI):
    def __init__(self, env):
        """
        Initialize a BookingAPI instance.

        Args:
            env (dict): A dictionary containing environment information, including the base API URL.
        """
        super().__init__(env)
        self.__booking_url = '/booking/'

    def get_booking_by_id(self, booking_id, headers=None):
        """
        Get booking details for a specific booking ID.

        Args:
            booking_id (int): The ID of the booking to retrieve.
            headers (dict, optional): Custom headers to be included in the request. Defaults to None.

        Returns:
            requests.Response: The response object containing the result of the GET request.
        """
        response = self.get(f'{self.__booking_url}{booking_id}', headers=headers)
        return response

    def get_bookings(self, headers=None):
        """
        Get a list of all bookings.

        Args:
            headers (dict, optional): Custom headers to be included in the request. Defaults to None.

        Returns:
            requests.Response: The response object containing the result of the GET request.
        """
        response = self.get(f'{self.__booking_url}', headers=headers)
        return response

    def create_booking(self, booking, headers=None):
        """
        Create a new booking.

        Args:
            booking (Booking): An instance of the Booking class representing the booking details.
            headers (dict, optional): Custom headers to be included in the request. Defaults to None.

        Returns:
            requests.Response: The response object containing the result of the POST request.
        """
        response = self.post(self.__booking_url, booking.get_dict(), headers=headers)
        return response

    def get_booking_by_response(self, response, headers=None):
        """
        Get booking details using the response object from a previous booking creation request.

        Args:
            response (requests.Response): The response object from a previous booking creation request.
            headers (dict, optional): Custom headers to be included in the request. Defaults to None.

        Returns:
            requests.Response: The response object containing the result of the GET request.
        """
        response_body_dict = json.loads(response.text)
        booking_id = response_body_dict['bookingid']
        get_response = self.get_booking_by_id(booking_id, headers=headers)
        return get_response

    def setup_token(self, env):
        """
        Set up authentication token for the API.

        Args:
            env (dict): A dictionary containing environment information, including the base API URL.
        """
        auth_api = AuthAPI(env)
        response = auth_api.create_token()
        response = json.loads(response.text)
        token = response['token']
        self.token = token

    def put_booking(self, booking_id, booking, headers=None):
        """
        Update an existing booking using a PUT request.

        Args:
            booking_id (int): The ID of the booking to be updated.
            booking (Booking): An instance of the Booking class representing the updated booking details.
            headers (dict, optional): Custom headers to be included in the request. Defaults to None.

        Returns:
            requests.Response: The response object containing the result of the PUT request.
        """
        return self.put(f'{self.__booking_url}{booking_id}', booking.get_dict(), headers=headers)

    def patch_booking(self, booking_id, params: dict, headers=None):
        """
        Update an existing booking using a PATCH request.

        Args:
            booking_id (int): The ID of the booking to be updated.
            params (dict): A dictionary containing the fields to be updated.
            headers (dict, optional): Custom headers to be included in the request. Defaults to None.

        Returns:
            requests.Response: The response object containing the result of the PATCH request.
        """
        return self.patch(f'{self.__booking_url}{booking_id}', params, headers=headers)

    def delete_booking(self, booking_id, headers=None):
        """
        Delete a booking.

        Args:
            booking_id (int): The ID of the booking to be deleted.
            headers (dict, optional): Custom headers to be included in the request. Defaults to None.

        Returns:
            requests.Response: The response object containing the result of the DELETE request.
        """
        return self.delete(f'{self.__booking_url}{booking_id}', headers=headers)
