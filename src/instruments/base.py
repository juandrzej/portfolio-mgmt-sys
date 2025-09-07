from abc import ABC, abstractmethod
from enum import StrEnum, auto

class InstrumentType(StrEnum):
    """Starting simple for now, we'll get deeper later."""
    # Core
    EQUITY_LONG = auto()
    EQUITY_SHORT = auto()
    BOND = auto()
    # Derivatives
    OPTION = auto()
    FUTURE = auto()
    # Other
    CURRENCY = auto()
    CASH = auto()

class FinancialInstrument(ABC):
    def __init__(self, symbol: str, price: float, quantity: int):
        self.symbol = symbol
        self.price = price
        self.quantity = quantity

        if not symbol or symbol.strip() == "":
            raise ValueError("Symbol cannot be empty")
        if price <= 0:
            raise ValueError("Price must be positive")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

    @abstractmethod
    def calculate_value(self) -> float:
        pass

    @abstractmethod
    def get_risk_metrics(self) -> dict:
        pass

    @abstractmethod
    def get_volatility(self) -> float:
        pass


