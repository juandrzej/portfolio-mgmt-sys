import pytest
from instruments.equity import Equity


class TestEquity:

    def test_calculate(self):
        stock = Equity("AAPL", 150.0, 100)
        assert stock.calculate_value() == 15000.0

    def test_calculate_extra(self):
        stock = Equity("AAPL", 150.0, 100, 1.5, "technology", 500)
        assert stock.calculate_value() == 15000.0

    def test_volatility_basic(self):
        stock = Equity("AAPL", 150.0, 100)
        assert stock.get_volatility() == 0.16

    def test_volatility_data(self):
        stock = Equity("AAPL", 150.0, 100, 1.5, "technology", 500)
        assert stock.get_volatility() == 0.16 * 1.5 * 1.4


    @pytest.mark.parametrize(
        "symbol,price,quantity",
        [
            ("", 10.0, 10),
            ("AAPL", -10.0, 10),
            ("AAPL", 10.0, -10)
        ]
    )
    def test_invalid_inputs(self, symbol, price, quantity):
        with pytest.raises(ValueError):
            Equity(symbol, price, quantity)





    @pytest.mark.skip
    def test_risk(self):
        pass
