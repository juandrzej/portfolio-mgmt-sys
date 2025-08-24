import pytest
from market_data.manager import MarketDataManager

def test_singleton_logic():
    # reset instance, only need for multiple singleton tests
    MarketDataManager._instance = None
    manager1 = MarketDataManager()
    manager2 = MarketDataManager()
    assert manager1 is manager2

@pytest.mark.parametrize('param', ['', None])
def test_empty_none_fetch(param):
    MarketDataManager._instance = None
    manager = MarketDataManager()
    with pytest.raises(ValueError):
        manager.fetch_data_daily(param)

def test_base_url():
    MarketDataManager._instance = None
    manager = MarketDataManager()
    assert manager.base_url == 'https://www.alphavantage.co/query'

def test_api_key():
    pass

