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
