import pytest
from instruments.equity import Equity


class TestEquity:

    def test_calculate(self):
        stock = Equity("AAPL", 150.0, 100)
        assert stock.calculate_value() == 15000.0

    def test_calculate_extra(self):
        stock = Equity("AAPL", 150.0, 100, 1.5, "technology", 500)
        assert stock.calculate_value() == 15000.0

    @pytest.mark.skip
    def test_risk(self):
        pass
