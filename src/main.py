from market_data.manager import MarketDataManager


def main():
    print("Hello from portfolio-mgmt-sys!")

    manager = MarketDataManager()
    daily_appl = manager.fetch_data_daily("AAPL")
    print(daily_appl)


if __name__ == "__main__":
    main()
