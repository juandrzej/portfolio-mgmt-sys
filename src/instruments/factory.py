from enum import Enum

class InstrumentType(Enum):
    """Initial instruments types listing, still researching these."""
    EQUITY = "equity"                    # Stocks, ETFs, equity indices. Use for cash equities.
    FIXED_INCOME = "fixed_income"        # Rates & Gov Bonds. Primary risk is interest rates.
    CREDIT = "credit"                    # Corporate bonds, CDS, loans. Primary risk is credit spread/default.
    COMMODITY = "commodity"              # Physical commodities (Oil, Gold, Corn) and their cash-settled futures.
    CURRENCY = "currency"                # Forex spot pairs. For FX derivatives, prefer DERIVATIVE.
    VOLATILITY = "volatility"            # VIX, volatility swaps, variance swaps. Direct vol exposure.
    DERIVATIVE = "derivative"            # Options, futures, swaps on any underlying. Use when the derivative nature is the key characteristic.
    ALTERNATIVE = "alternative"          # Real estate, infrastructure, private equity, illiquid assets.
    CASH = "cash"                        # Cash deposits, money market funds, repos.


class InstrumentFactory:
    """Creates different types of financial instruments"""
    pass
