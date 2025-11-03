from typing import Any


class User:
    """
    A user of the portfolio system.

    id : int
        Unique user identifier.
    username : str
        The user's username.
    email : str
        The user's email address.
    password : str
        The user's password (should be stored hashed in production).
    portfolios : list
        List of the user's portfolio objects.

    """

    def __init__(self: "User", user_id: int, username: str, email: str, password: str) -> None:
        """Initialize a User."""
        self.id: int = user_id
        self.username: str = username
        self.email: str = email
        self.password: str = password
        self.portfolios: list[Any] = []


class Portfolio:
    """
    A portfolio owned by a user.

    owner_id : int
        The id of the user who owns the portfolio.
    name : str
        The portfolio name.
    securities : list
        List of securities held in the portfolio.

    """

    def __init__(self, owner_id: int, name: str, securities: list[Any]) -> None:
        """
        Initialize a Portfolio.

        owner_id : int
            The id of the portfolio owner.
        name : str
            The portfolio name.
        """
        self.owner_id: int = owner_id
        self.name: str = name
        self.securities: list[Any] = []
