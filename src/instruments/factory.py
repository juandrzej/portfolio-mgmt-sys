from abc import ABC, abstractmethod
from enum import Enum, auto

class InstrumentType(Enum):
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
    def calculate_value(self):
        pass

    @abstractmethod
    def get_risk_metrics(self):
        pass


class InstrumentFactory:
    """Creates different types of financial instruments"""
    pass
