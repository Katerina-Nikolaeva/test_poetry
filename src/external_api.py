from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_BASE_URL = "https://api.apilayer.com/currency_data/convert"
# API_BASE_URL = "https://api.apilayer.com/exchangerates_data/convert"
api_key = os.getenv("API_KEY")
if not api_key:
    raise RuntimeError("No API key loaded from .env")
print(f"API key OK: {api_key[:10]}...")


def get_exchange_rate(from_currency: str, to_currency: str) -> float:
    headers = {"apikey": api_key}
    params = {"from": from_currency, "to": to_currency, "amount": 1}

    response = requests.get(API_BASE_URL, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()

    # Пример структуры (может отличаться по версии API):
    # {"success": True, "result": 90.5}
    return float(data["result"])


def get_convert(transaction_conv: dict):
    amount = float(transaction_conv["operationAmount"]["amount"])
    currency_name = transaction_conv["operationAmount"]["currency"]["name"]

    if currency_name == "RUB":
        return amount
    elif currency_name in ["USD", "EUR"]:
        exchange_rate = get_exchange_rate(currency_name, "RUB")
        return amount * exchange_rate
    else:
        raise ValueError(f"Валюта {currency_name} не поддерживается")


if __name__ == "__main__":
    transaction_conv = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    print(get_convert(transaction_conv))
