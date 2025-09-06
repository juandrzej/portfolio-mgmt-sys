from base import FinancialInstrument

class Equity(FinancialInstrument):
    def __init__(self, symbol: str, price: float, quantity: int, beta: float, sector: str, dividend: int = 0):
        super().__init__(symbol, price, quantity)
        self.beta = beta
        self.sector = sector
        self.dividend = dividend

    def calculate_value(self) -> float:
        return self.price * self.quantity

    def get_risk_metrics(self) -> dict:
        return {}
