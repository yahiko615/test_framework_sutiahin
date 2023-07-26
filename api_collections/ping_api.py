from utilities.api_utilities.base_api import BaseAPI

class PingAPI(BaseAPI):
    def __init__(self, env):
        """
        Initialize a PingAPI instance.

        Args:
            env (dict): A dictionary containing environment information, including the base API URL.
        """
        super().__init__(env)
        self._ping_url = '/ping'

    def ping(self):
        """
        Send a ping request to the API.

        Returns:
            requests.Response: The response object containing the result of the ping request.
        """
        response = self.get(self._ping_url)
        return response
