import pytest
from market_data.manager import MarketDataManager

class TestMarketDataManager:

    #NOTE:This runs before every test method in this class, freaking amazing
    def setup_method(self):
        """Reset instance (only need for multiple singleton tests)"""
        MarketDataManager._instance = None

    def test_singleton_logic(self):
        manager1 = MarketDataManager()
        manager2 = MarketDataManager()
        assert manager1 is manager2

    @pytest.mark.parametrize('param', ['', None])
    def test_empty_none_fetch(self, param):
        manager = MarketDataManager()
        with pytest.raises(ValueError):
            manager.fetch_data_daily(param)

    def test_base_url(self):
        manager = MarketDataManager()
        assert manager.base_url == 'https://www.alphavantage.co/query'

    def test_api_key(self):
        manager = MarketDataManager()
        assert manager.api_key is not None
        assert len(manager.api_key) > 0


