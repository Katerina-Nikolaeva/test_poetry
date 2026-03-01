import os
import requests


API_BASE_URL = "https://api.apilayer.com/exchangerates_data/"
API_KEY = os.getenv("EXCHANGE_RATES_API_KEY")


def fetch_exchange_rate(to_currency: str, from_currency: str) -> float:
    """
    Получает текущий курс валют от внешнего API.

    :param to_currency: Целевая валюта (например, RUB)
    :param from_currency: Исходная валюта (например, USD или EUR)
    :return: Курс конвертации (например, 1 USD = 70 RUB)
    """
    url = f"{API_BASE_URL}/latest?access_key={API_KEY}¤cies={to_currency}&base={from_currency}"
    response = requests.get(url)
    response.raise_for_status()  # Проверяем успешность запроса

    data = response.json()

    return data['quotes'].get(f'{from_currency}{to_currency}')
