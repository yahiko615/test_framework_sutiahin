import requests


class BaseAPI:
    def __init__(self, env):
        """
        Initialize a BaseAPI instance.

        Args:
            env (dict): A dictionary containing environment information, including the base API URL.
        """
        self.__token = None
        self.__base_url = env['base_api']
        self.__headers = {'Accept': '*/*', 'Content-Type': 'application/json'}
        self.__request = requests

    @property
    def token(self):
        """
        Get the authentication token.

        Returns:
            str: The authentication token.
        """
        return self.__token

    @token.setter
    def token(self, new_token):
        """
        Set the authentication token and update the 'Cookie' header.

        Args:
            new_token (str): The new authentication token.
        """
        self.__token = new_token
        self.__headers['Cookie'] = f'token={self.__token}'

    def get(self, url, headers=None):
        """
        Perform a GET request to the API.

        Args:
            url (str): The API endpoint to send the GET request to.
            headers (dict, optional): Custom headers to be included in the request. Defaults to None.

        Returns:
            requests.Response: The response object of the GET request.
        """
        if headers is None:
            headers = self.__headers
        return self.__request.get(f'{self.__base_url}{url}', headers=headers)

    def post(self, url, body, headers=None):
        """
        Perform a POST request to the API.

        Args:
            url (str): The API endpoint to send the POST request to.
            body (dict): The JSON body to be included in the request.
            headers (dict, optional): Custom headers to be included in the request. Defaults to None.

        Returns:
            requests.Response: The response object of the POST request.
        """
        if headers is None:
            headers = self.__headers
        return self.__request.post(f'{self.__base_url}{url}', json=body, headers=headers)

    def put(self, url, body, headers=None):
        """
        Perform a PUT request to the API.

        Args:
            url (str): The API endpoint to send the PUT request to.
            body (dict): The JSON body to be included in the request.
            headers (dict, optional): Custom headers to be included in the request. Defaults to None.

        Returns:
            requests.Response: The response object of the PUT request.
        """
        if headers is None:
            headers = self.__headers
        return self.__request.put(f'{self.__base_url}{url}', json=body, headers=headers)

    def patch(self, url, body, headers=None):
        """
        Perform a PATCH request to the API.

        Args:
            url (str): The API endpoint to send the PATCH request to.
            body (dict): The JSON body to be included in the request.
            headers (dict, optional): Custom headers to be included in the request. Defaults to None.

        Returns:
            requests.Response: The response object of the PATCH request.
        """
        if headers is None:
            headers = self.__headers
        return self.__request.patch(f'{self.__base_url}{url}', json=body, headers=headers)

    def delete(self, url, headers=None):
        """
        Perform a DELETE request to the API.

        Args:
            url (str): The API endpoint to send the DELETE request to.
            headers (dict, optional): Custom headers to be included in the request. Defaults to None.

        Returns:
            requests.Response: The response object of the DELETE request.
        """
        if headers is None:
            headers = self.__headers
        return self.__request.delete(f'{self.__base_url}{url}', headers=headers)
