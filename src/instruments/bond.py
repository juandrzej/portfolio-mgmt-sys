from instruments.base import FinancialInstrument

class Bond(FinancialInstrument):
    def __init__(self, symbol: str, price: float, quantity: int, coupon_rate: float, maturity: str, credit_rating: str = "AAA"):
        super().__init__(symbol, price, quantity)
        self._coupon_rate = coupon_rate
        self._maturity = maturity
        self._credit_rating = credit_rating

    def calculate_value(self) -> float:
        return self.price * self.quantity * (self._coupon_rate + 1)

    def get_risk_metrics(self) -> dict:
        """Not implemented yet."""
        return {}

    def get_volatility(self) -> float:
        rating_volatility = {
            "AAA": 0.02,
            "AA": 0.03,
            "A": 0.04,
            "BBB": 0.06,
            "BB": 0.10,
            "B": 0.15,
            "CCC": 0.25,
            "D": 0.40
        }

        #TODO: add duration to calcs (counted from maturity date)
        return rating_volatility[self._credit_rating]

