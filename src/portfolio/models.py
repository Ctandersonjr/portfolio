class securities:
    """ A security held in a portfolio. """

    def __init__(self, symbol: str, quantity: int, purchase_price: float) -> None:
        """ Initialize a Security. """
        self.symbol = symbol
        self.quantity = quantity
        self.purchase_price = purchase_price

class Portfolio:
    """ A portfolio owned by a user. """

    def __init__(self, owner_id: int, name: str, securities: dict[securities]) -> None:
        """ Initialize a Portfolio. """
        self.owner_id = owner_id
        self.name = name
        self.securities = securities # type: ignore
class User:
    """ A user of the portfolio system. """

    def __init__(self, user_id: int, username: str, email: str, password: str) -> None:
        """Initialize a User."""
        self.id = user_id
        self.username = username
        self.email = email
        self.password = password


class SecurityService:
    """A class to add securities to a portfolio."""

    def add_security(self, portfolio: Portfolio, security: dict[securities]) -> None:
        """ Add a security to the given portfolio. """
        portfolio.securities[securities.symbol] = securities

    def delete_security(self, portfolio: Portfolio, security: dict[securities]) -> None:
        """ Delete a security from the given portfolio. """
        if security in portfolio.securities:
            del portfolio.securities[securities.symbol]

class GraphicalView:
    """ Graphical views of portfolio data. """

    def display_graph(self, portfolio: Portfolio) -> None:       
        # Placeholder for graphical representation logic
        print(f"Displaying graphical view for portfolio: {portfolio.name}")

class TaxData:
    """Tax data related to portfolios."""

    def calculate_tax(self, portfolio: Portfolio) -> float:
        return 0.0