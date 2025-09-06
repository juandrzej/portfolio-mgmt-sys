from base import FinancialInstrument

class Equity(FinancialInstrument):
    def __init__(self, symbol: str, price: float, quantity: int, beta: float = 1.0, sector: str = "", dividend: int = 0):
        super().__init__(symbol, price, quantity)
        self._beta = beta
        self._sector = sector.lower()
        self._dividend = dividend

    def calculate_value(self) -> float:
        return self.price * self.quantity

    def get_risk_metrics(self) -> dict:
        """Not implemented yet."""
        return {}

    def get_volatility(self) -> float:
        base_market_vol = 0.16  # S&P 500 ~16% annual volatility

        # Sector multipliers
        sector_multipliers = {
            "technology": 1.4,
            "healthcare": 1.2,
            "financials": 1.3,
            "utilities": 0.7,
            "consumer_staples": 0.8,
            "energy": 1.5,
            "real_estate": 1.1,
            "industrials": 1.0,
            "materials": 1.2,
            "consumer_discretionary": 1.3,
            "telecommunications": 0.9
        }

        return base_market_vol * self._beta * sector_multipliers.get(self._sector, 1.0)
