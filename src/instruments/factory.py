from instruments.base import FinancialInstrument, InstrumentType
from instruments.bond import Bond
from instruments.equity import Equity


class InstrumentFactory:
    """Creates different types of financial instruments"""

    @staticmethod
    def create_instrument(instrument_type: InstrumentType, **kwargs) -> FinancialInstrument:
        match instrument_type:
            case InstrumentType.EQUITY_LONG | InstrumentType.EQUITY_SHORT:
                return Equity(
                    symbol=kwargs["symbol"],
                    price=kwargs["price"],
                    quantity=kwargs["quantity"],
                    beta=kwargs.get("beta", 1.0),
                    sector=kwargs.get("sector", ""),
                    dividend=kwargs.get("dividend", 0),
                )
            case InstrumentType.BOND:
                return Bond(
                    symbol=kwargs["symbol"],
                    price=kwargs["price"],
                    quantity=kwargs["quantity"],
                    coupon_rate=kwargs["coupon_rate"],
                    maturity=kwargs["maturity"],
                    credit_rating=kwargs.get("credit_rating", "AAA")
                )
            case _:
                raise ValueError(f"Unknown instrument type: {instrument_type}")
