import yfinance as yf
import numpy as np

class user:
    def person(self, user_id, username, email, password):
        self.id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.portfolios = []

class authentication:
    def login(self, username, password)
        pass

    def authorize(self, user_id, portfolio_owner_id):
        return user_id == portfolio_owner_id

class assets:
     def securities(self, symbol, shares, purchase_price):
        self.symbol = symbol
        self.shares = shares
        self.purchase_price = purchase_price

     def current_value(self, current_price):
        return self.shares * current_price

class portfolio:
    def portfolio(self, owner_id, name):
        self.owner_id = owner_id
        self.name = name
        self.assets = []

     def add_security(self, security):
        self.securities.append(security)

    def remove_security(self, symbol):
        self.securities = [s for s in self.holdings if s.symbol != symbol]
    
class portfolioAnalytics:
    def __init__(self, portfolio):
        self.portfolio = portfolio

    def calculate_total_value(self, prices):
        return sum(h.current_value(prices.get(h.symbol, 0)) for h in self.portfolio.holdings)

    def calculate_gains(self, prices):
        invested = sum(h.shares * h.purchase_price for h in self.portfolio.holdings)
        return self.calculate_total_value(prices) - invested

    def calculate_risk(self, historical_returns):
        return np.std(historical_returns)

class TaxReport:
    def __init__(self, portfolio, tax_year):
        self.portfolio = portfolio
        self.tax_year = tax_year

    def generate_form(self):
        return {
            "year": self.tax_year,
            "total_gains": 0,
            "total_losses": 0,
        }

class MarketData:
    def get_historical_data(self, symbol, period="1y"):
        data = yf.download(symbol, period=period, progress=False)
        return data

class Visualization:
    pass

