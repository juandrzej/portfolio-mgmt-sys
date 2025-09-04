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


class InstrumentFactory:
    """Creates different types of financial instruments"""
    pass
