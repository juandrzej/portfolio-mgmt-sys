from market_data.manager import MarketDataManager

def test_singleton_basic():
    manager1 = MarketDataManager()
    manager2 = MarketDataManager()
    assert manager1 is manager2
