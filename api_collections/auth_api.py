from utilities.api_utilities.base_api import BaseAPI


class AuthAPI(BaseAPI):
    def __init__(self, env):
        """
        Initialize an AuthAPI instance.

        Args:
            env (dict): A dictionary containing environment information, including the base API URL.
        """
        super().__init__(env)
        self.__auth_url = '/auth'
        self.__credentials = env["credentials"]

    def create_token(self, credentials=None):
        """
        Create an authentication token using the provided credentials.

        Args:
            credentials (dict, optional): A dictionary containing the user's credentials.
                                          Defaults to None, in which case the credentials from
                                          the instance's __credentials attribute will be used.

        Returns:
            requests.Response: The response object containing the result of the token creation request.
        """
        if credentials is None:
            credentials = self.__credentials
        response = self.post(self.__auth_url, credentials)
        return response
