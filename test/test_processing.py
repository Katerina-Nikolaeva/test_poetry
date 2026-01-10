from typing import List

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def coll() -> List[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]


# Сортировка даты по возрастанию
def test_sort_by_date_ascending(coll: List[dict]) -> None:
    expected_result = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},  # самая ранняя дата
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},  # самая поздняя дата
    ]
    result = sort_by_date(coll, False)
    assert result == expected_result


# Сортировка даты по убыванию
def test_sort_by_date_desc(coll: List[dict]) -> None:
    expected_result = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},  # самая поздняя дата
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},  # самая ранняя дата
    ]
    result = sort_by_date(coll, True)
    assert result == expected_result


# Одинаковые даты
@pytest.fixture
def coll_same_date() -> List[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_same(coll_same_date: List[dict]) -> None:
    expected_result = coll_same_date[:]  # Копируем коллекцию, чтобы сравнить её с собой
    result = sort_by_date(coll_same_date)
    assert result == expected_result


# Некорректные даты
@pytest.fixture
def incorrect_dates() -> List[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2023-13-01"},  # месяц вне диапазона
        {"id": 939719570, "state": "PENDING", "date": "неверная_дата"},  # строка вместо даты
        {"id": 594226727, "state": "CANCELED", "date": "2023-01-32"},  # день вне диапазона
    ]


# Тест на обработку некорректных дат
def test_sort_by_date_incorrect_dates(incorrect_dates: List[dict]) -> None:
    with pytest.raises(ValueError):
        sort_by_date(incorrect_dates, True)


# Тестирование фильтрации списка словарей по заданному статусу
@pytest.fixture
def coll_state() -> List[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state(coll_state: List[dict]) -> None:
    expected_result = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    result = filter_by_state(coll_state, "EXECUTED")
    assert result == expected_result


# Проверка работы функции при отсутствии словарей с указанным статусом state в списке
@pytest.fixture
def coll_without_state() -> List[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# Тест на отсутствие словарей с указанным статусом
def test_filter_by_state_not_found(coll_without_state: List[dict]) -> None:
    expected_result: List[dict] = []  # Должен вернуть пустой список, так как заданного статуса нет
    result = filter_by_state(coll_without_state, "UNKNOWN_STATE")  # пытаемся искать неизвестный статус
    assert result == expected_result


# Фикстура с основными данными для параметризированного теста для разных статусов
@pytest.fixture
def coll_state_all() -> List[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# Параметризированный тест с названиями (input, expected_result)
@pytest.mark.parametrize(
    "state,expected_result",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ("UNKNOWN_STATUS", []),  # Ожидаем пустой список, так как такого статуса нет
    ],
)
def test_filter_by_state_parameterized(coll_state_all: List[dict], state: str, expected_result: List[dict]) -> None:
    result = filter_by_state(coll_state_all, state)
    assert result == expected_result
