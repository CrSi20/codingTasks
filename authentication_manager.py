from database_manager import DatabaseManager


class AuthenticationManager:
    """ Class that allows the user to authenticate
    """

    def __init__(self):
        """ Instantiates an object
        """
        self.database_manager = DatabaseManager()

    def create_user(self, user_id: str, password: str):
        """Creates a user.

        Arguments:
        - user_id: str - the user id
        - password: str - the password
        """
        self.database_manager.create_user(user_id, password)

    def authenticate_user(self, user_id: str, password: str) -> bool:
        """ Function that authenticates the user.

        Arguments:
        - user_id: str - the user id
        - password: str - the password

        Returns: True if the user exists and the password is correct,
                otherwise False
        """

        return self.database_manager.check_user(user_id, password)
