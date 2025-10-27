import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Charge les variables depuis le fichier .env
load_dotenv()

# Lecture des variables
COINGECKO_API_URL = os.getenv("COINGECKO_API_URL")
DEFAULT_VS_CURRENCY = os.getenv("DEFAULT_VS_CURRENCY", "usd")
TOP_N_COINS = int(os.getenv("TOP_N_COINS", 10))

def fetch_crypto_data(vs_currency=DEFAULT_VS_CURRENCY, top_n=TOP_N_COINS):
    params = {
        "vs_currency": vs_currency,
        "order": "market_cap_desc",
        "per_page": top_n,
        "page": 1,
        "sparkline": False
    }
    response = requests.get(COINGECKO_API_URL, params=params)
    response.raise_for_status()  # pour gérer les erreurs HTTP
    df = pd.DataFrame(response.json())
    df = df[["id", "symbol", "name", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"]]
    return df
