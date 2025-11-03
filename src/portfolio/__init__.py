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
        self.securities: list[Any] = securities

class AddSecurity:
    """A class to add securities to a portfolio."""

    def add_security(self: "AddSecurity", portfolio: Portfolio, security: list[Any]) -> None:
        """
        Add a security to the given portfolio.

        portfolio : Portfolio
            The portfolio to which the security will be added.
        security : Any
            The security to add to the portfolio.
        """
        portfolio.securities.append(security)

class DeleteSecurity:
    """A class to delete securities from a portfolio."""

    def delete_security(self: "DeleteSecurity", portfolio: Portfolio, security: list[Any]) -> None:
        """
        Delete a security from the given portfolio.

        portfolio : Portfolio
            The portfolio from which the security will be deleted.
        security : Any
            The security to delete from the portfolio.
        """
        if security in portfolio.securities:
            portfolio.securities.remove(security)

class GraphicalView:
    """A class to represent graphical views of portfolio data."""

    def display_graph(self: "GraphicalView", portfolio: Portfolio) -> None:
        """
        Display a graphical representation of the portfolio data.

        portfolio : Portfolio
            The portfolio whose data will be graphically represented.
        """
        # Placeholder for graphical representation logic
        print(f"Displaying graphical view for portfolio: {portfolio.name}")

class TaxData:
    """A class to handle tax data related to portfolios."""

    def calculate_tax(self: "TaxData", portfolio: Portfolio) -> float:
        """
        Calculate tax based on the portfolio data.

        portfolio : Portfolio
            The portfolio for which tax will be calculated.

        Returns
        -------
        float
            The calculated tax amount.
        """

        return 0.0