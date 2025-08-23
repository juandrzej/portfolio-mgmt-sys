import httpx
import os
from dotenv import load_dotenv


class MarketDataManager:
    """Singleton class to process all API data calls."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self) -> None:
        #NOTE:prevents re-initialization
        if self._initialized:
            return

        # Load environment variables, declare static data and validate api key
        load_dotenv()
        self.api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
        self.base_url = 'https://www.alphavantage.co/query'
        if not self.api_key:
            raise ValueError('Alpha Vantage api key failed to load from .env')

        self._initialized = True

    def fetch_data_daily(self, equity: str) -> dict:
        """Fetch daily data for given equity symbol."""
        if not equity:
            raise ValueError('Equity symbol cannot be empty')

        parameters = {
            "function": "TIME_SERIES_DAILY",
            "symbol": equity.upper(),
            "apikey": self.api_key
        }

        response = httpx.get(url=self.base_url, params=parameters)
        return response.json()
