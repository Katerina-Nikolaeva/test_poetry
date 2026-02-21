from typing import Dict, Iterator


def filter_by_currency(transactions: list, currency_code: str) -> Iterator[Dict]:
    """
    Фильтрует транзакции по заданному коду валюты.

    :param transactions: Список словарей, каждый из которых представляет одну транзакцию.
    :param currency_code: Код валюты, по которой нужно произвести фильтрацию.
    :return: Итератор, выдающий подходящие транзакции.
    """
    for transaction in transactions:
        amount_details = transaction.get("operationAmount", {})
        currency_details = amount_details.get("currency", {})
        current_code = currency_details.get("code")

        if current_code == currency_code:
            yield transaction


def transaction_descriptions(transactions: list) -> Iterator[Dict]:
    """
    Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.

    :param transactions: список словарей, где каждый словарь описывает отдельную транзакцию
    :yield: description (строка) — описание очередной транзакции
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: str = "0000000000000001", stop: str = "9999999999999999") -> Iterator[str]:
    """
    Генератор, выдающий номера банковских карт в формате XXXX XXXX XXXX XXXX.
    start и end — начальный и конечный номера карт в формате строки.
    """
    start_num = int(start)
    end_num = int(stop)

    # Перебираем номера карточек в указанном диапазоне
    for num in range(start_num, end_num + 1):
        # Форматируем карточку: разбиваем каждую группу по 4 цифры
        formatted_card = "{:016}".format(num)
        parts = [formatted_card[i : i + 4] for i in range(0, len(formatted_card), 4)]
        yield " ".join(parts)
