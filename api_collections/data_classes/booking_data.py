import json


class Booking:
    """Represents booking information for a customer."""

    def __init__(self, **kwargs):
        """
        Initialize the Booking object.

        Args:
            **kwargs: Keyword arguments to set booking details.
                      Available arguments: firstname, lastname, totalprice,
                      depositpaid, bookingdates (dictionary with keys checkin
                      and checkout).
        """
        self.firstname = 'Mary' if 'firstname' not in kwargs else kwargs['firstname']
        self.lastname = 'Smith' if 'lastname' not in kwargs else kwargs['lastname']
        self.totalprice = 937 if 'totalprice' not in kwargs else kwargs['totalprice']
        self.depositpaid = False if 'depositpaid' not in kwargs else kwargs['depositpaid']
        self.bookingdates = {"checkin": "2022-10-13", "checkout": "2023-04-10"} \
            if 'bookingdates' not in kwargs else kwargs['bookingdates']

    def update_data(self, **kwargs):
        """
        Update the booking data with new values.

        Args:
            **kwargs: Keyword arguments to update booking details.
        """
        self.__dict__.update(**kwargs)

    def get_json(self):
        """
        Get the JSON representation of the Booking object.

        Returns:
            str: A JSON string representing the booking details.
        """
        return json.dumps(self.__dict__)

    def get_dict(self):
        """
        Get the dictionary representation of the Booking object.

        Returns:
            dict: A dictionary containing the booking details.
        """
        return self.__dict__

    def get_dict_without_id(self):
        """
        Get the dictionary representation of the Booking object without the 'bookingid' key.

        Returns:
            dict: A dictionary containing the booking details excluding 'bookingid'.
        """
        self.__dict__.pop('bookingid', None)
        return self.__dict__

    @classmethod
    def from_json(cls, json_data):
        """
        Create a Booking object from a JSON string.

        Args:
            json_data (str): A JSON string containing booking details.

        Returns:
            Booking: A new Booking object with data from the JSON string.
        """
        data_dict = json.loads(json_data)
        return cls(**data_dict)
