from typing import Any

from portfolio import Portfolio, User  # type: ignore


def test_view_current_portfolio_holdings() -> None:
    """Test viewing current portfolio holdings."""
    # Arrange
    logged_in_user = User( 1, "cedric", "cedric@gmail.com", "cedspassword")
    portfolio = Portfolio(logged_in_user, "Retirement Fund", [])
    # Act
    holdings: list[Any] = portfolio.securities
    # Assert
    securities: list[Any] = []
    assert securities == holdings

def test_add_security_to_portfolio() -> None:
    """Test adding a security to the portfolio."""
    # Arrange
    logged_in_user = User( 1, "cedric", "cedric@gmail.com", "cedspassword")
    portfolio = Portfolio(logged_in_user, "Retirement Fund", [])
    # Act
    portfolio.securities.append("AAPL")
    # Assert
    assert ("AAPL") in portfolio.securities

def test_delete_security_from_portfolio() -> None:
    """Test deleting a security from the portfolio."""
    # Arrange
    logged_in_user = User( 1, "cedric", "cedric@gmail.com", "cedspassword")
    portfolio = Portfolio(logged_in_user, "Retirement Fund", ["AAPL"])
    # Act
    portfolio.securities.remove("AAPL")
    # Assert
    assert ("AAPL") not in portfolio.securities