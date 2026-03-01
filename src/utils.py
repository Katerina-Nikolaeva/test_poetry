from dotenv import load_dotenv
import requests
import json
import os


def load_and_convert_transactions(file_path):
    """
    Читает JSON-файл с финансовыми транзакциями и возвращает список словарей.
    Если валюта транзакции не рубли, выполняет конвертацию через API.

    :param file_path: Путь до JSON-файла с транзакциями
    :return: Список словарей с данными о транзакциях, все суммы приведены к рублёвому эквиваленту
    """
    load_dotenv()
    api_key = os.getenv("API_KEY", "")

    try:
        # Читаем файл
        with open(file_path, mode='r', encoding='utf-8') as file:
            transactions = json.load(file)

        # Проверяем, что это список
        if not isinstance(transactions, list):
            return []

        # Обрабатываем каждую транзакцию
        for transaction in transactions:
            currency_code = transaction['operationAmount']['currency']['code']
            amount = float(transaction['operationAmount']['amount'])

            if currency_code != "RUB":
                # Формируем URL
                url = (f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount="
                       f"{amount}")
                headers = {'apikey': api_key}

                try:
                    # Отправляем запрос к API
                    response = requests.get(url, headers=headers)
                    response.raise_for_status()    # Проверяем успешность запроса

                    # Получаем результат конвертации
                    result = response.json()['result']
                    transaction['operationAmount']['amount'] = result
                    transaction['operationAmount']['currency']['code'] = "RUB"
                except requests.RequestException as e:
                    # Обрабатываем ошибки сети и API
                    print(f"Ошибка запроса к API: {e}")

        return transactions

    except FileNotFoundError:
        print("Файл не найден.")
        return []
    except json.JSONDecodeError:
        print("Ошибка парсинга JSON.")
        return []
    except Exception as ex:
        print(f"Ошибка при обработке транзакций: {ex}")
        return []
