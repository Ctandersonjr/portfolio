from typing import NewType

UserID = NewType("UserID", int)
Username = NewType("Username", str)
Email = NewType("Email", str)
Password = NewType("Password", str)

class User:
    """ A user of the portfolio system. """

    def __init__(self, user_id: UserID, username: Username, email: Email, password: Password) -> None:
        """Initialize a User."""
        self.id = user_id
        self.username = username
        self.email = email
        self.password = password
