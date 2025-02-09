import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def check_currency(transaction: dict) -> float:
    """Принимает транзакцию и конвертирует из иностранной валюты в РУБЛИ с запросом на API сайт"""
    amount = float(transaction["operationAmount"]["amount"])  # получение суммы траты
    currency = transaction["operationAmount"]["currency"]["code"]  # получение валюты
    if currency != "RUB":
        url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"
        headers = {"apikey": f"{API_KEY}"}
        response = requests.get(url, headers=headers)
        return round(response.json()["rates"]["RUB"] * amount, 2)
    return amount
