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

    @abstractmethod
    def calculate_value(self) -> float:
        pass

    @abstractmethod
    def get_risk_metrics(self) -> dict:
        pass


