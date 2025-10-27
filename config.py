import os
from dotenv import load_dotenv

load_dotenv()

COINGECKO_API_URL = os.getenv("COINGECKO_API_URL")
DEFAULT_VS_CURRENCY = os.getenv("DEFAULT_VS_CURRENCY", "usd")
TOP_N_COINS = int(os.getenv("TOP_N_COINS", 10))
