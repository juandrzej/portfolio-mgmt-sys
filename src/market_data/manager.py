import httpx
import os
from dotenv import load_dotenv

# Load environment variables from a .env file and declare static data
load_dotenv()
API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
URL = 'https://www.alphavantage.co/query'


class MarkerDataManager:
    """Singleton class to process all API data calls."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        pass

    def fetch_data_daily(self, equity: str) -> None:
        parameters = {
            "function": "TIME_SERIES_DAILY",
            "symbol": equity,
            "apikey": API_KEY
        }
        response = httpx.get(url=URL, params=parameters)
        return response.json()
