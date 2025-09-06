from base import FinancialInstrument

class Bond(FinancialInstrument):
    def __init__(self, symbol: str, price: float, quantity: int, coupon_rate: float, maturity: str):
        super().__init__(symbol, price, quantity)
        self.coupon_rate = coupon_rate
        self.maturity = maturity

    def calculate_value(self) -> float:
        return self.price * self.quantity * (self.coupon_rate + 1)

    def get_risk_metrics(self) -> dict:
        return {}
