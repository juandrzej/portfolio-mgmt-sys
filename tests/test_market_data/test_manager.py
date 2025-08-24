import pytest
from market_data.manager import MarketDataManager

def test_singleton_basic():
    # reset instance, only need for multiple singleton tests
    MarketDataManager._instance = None

    manager1 = MarketDataManager()
    manager2 = MarketDataManager()
    assert manager1 is manager2

def test_empty_none_fetch():
    MarketDataManager._instance = None

    manager = MarketDataManager()

    with pytest.raises(ValueError):
        manager.fetch_data_daily("")

    with pytest.raises(ValueError):
        manager.fetch_data_daily(None)
