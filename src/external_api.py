from dotenv import load_dotenv
import os
import requests

API_BASE_URL = "https://api.apilayer.com/exchangerates_data/latest"
load_dotenv()
api_key = os.getenv("EXCHANGE_RATES_API_KEY")


def get_exchange_rate(from_currency: str, to_currency: str) -> float:
    """
    Получает текущий курс обмена валют с использованием apilayer API.

    :param from_currency: Базовая валюта (например, USD)
    :param to_currency: Цель конвертации (например, RUB)
    :return: Текущий курс конвертации
    """
    url = f"{API_BASE_URL}?access_key={api_key}&base={from_currency}&symbols={to_currency}"
    response = requests.get(url)
    response.raise_for_status()  # Проверка успешного статуса запроса
    rates = response.json()["rates"]
    return rates[to_currency]


def get_convert(transaction_conv):
    """
    Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях.

    :param transaction_conv: Транзакция с указанием суммы и валюты
    :return: Сумма транзакции в рублях (float)
    """
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
