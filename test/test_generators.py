import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_filter_by_currency_existing(sample_transactions):
    """Тестирование фильтрации по существующей валюте."""
    filtered = list(filter_by_currency(sample_transactions, "USD"))
    assert len(filtered) == 3  # Три транзакции с USD
    ids = sorted([item["id"] for item in filtered])
    assert ids == [142264268, 895315941, 939719570]  # Сортируем id для сравнения


def test_filter_by_currency_no_matching_transactions(sample_transactions):
    """Тестирование случая отсутствия транзакций с заданной валютой."""
    filtered = list(filter_by_currency(sample_transactions, "GBP"))
    assert len(filtered) == 0


def test_filter_by_currency_empty_transaction_list() -> None:
    """Тестирование с пустым списком транзакций."""
    empty_transactions = []
    filtered = list(filter_by_currency(empty_transactions, "USD"))
    assert len(filtered) == 0


def test_filter_by_currency_invalid_input():
    """Тестирование передачи некорректных аргументов."""
    with pytest.raises(TypeError):
        list(filter_by_currency(None, "USD"))


# Тест №1: проверка работы с несколькими транзакциями
def test_transaction_descriptions_multiple():
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    actual_descriptions = list(transaction_descriptions(transactions))
    assert actual_descriptions == expected_descriptions


# Тест №2: проверка работы с одним элементом
def test_transaction_descriptions_single():
    transactions = [{"id": 1, "description": "Покупка билетов"}]
    expected_descriptions = ["Покупка билетов"]
    actual_descriptions = list(transaction_descriptions(transactions))
    assert actual_descriptions == expected_descriptions


# Тест №3: проверка работы с пустым списком транзакций
def test_transaction_descriptions_empty():
    transactions = []
    expected_descriptions = []
    actual_descriptions = list(transaction_descriptions(transactions))
    assert actual_descriptions == expected_descriptions


# Тест №1: Базовый тест с первым номером карты
def test_card_number_generator_first():
    gen = card_number_generator()
    first_card = next(gen)
    assert first_card == "0000 0000 0000 0001"


# Тест №2: Генерируем последний номер карты
def test_card_number_generator_last():
    last_gen = card_number_generator(stop="0000000000000002")
    cards = list(last_gen)
    assert cards[-1] == "0000 0000 0000 0002"


# Тест №3: Проверка правильного форматирования номера карты
def test_card_number_generator_formatting():
    gen = card_number_generator()
    first_card = next(gen)
    assert first_card.count(" ") == 3  # Должно быть три пробела между группами цифр
    assert all(len(part) == 4 for part in first_card.split())  # Каждая группа должна содержать 4 цифры


# Тест №4: Граничный случай, когда диапазон состоит всего из одного элемента
def test_one_element_range():
    single_gen = card_number_generator(start="0000000000000001", stop="0000000000000001")
    cards = list(single_gen)
    assert len(cards) == 1
    assert cards[0] == "0000 0000 0000 0001"


# Тест №5: Граничный случай — старт больше конца
def test_start_greater_than_stop():
    gen = card_number_generator(start="0000000000000002", stop="0000000000000001")
    cards = list(gen)
    assert len(cards) == 0


# Тест №6: Генерация произвольного количества карт
def test_large_range():
    large_gen = card_number_generator(start="0000000000000001", stop="0000000000000003")
    cards = list(large_gen)
    assert len(cards) == 3
    assert cards == ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]
