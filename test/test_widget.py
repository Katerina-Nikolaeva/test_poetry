import pytest

from src.widget import get_date, mask_account_card


# Параметризация теста для карты или счета
@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("Счет 73654108430135874305", "Счет **4305"),  # Маскирование счета или карты
        ("Visa 7000792289606361", "Visa 7000 79** **** 6361"),  # Маскирование корректного типа карты
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),  # Маскирование корректного типа карты
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),  # Маскирование корректного типа карты
        ("Mastercard 7000792289606361", "Mastercard 7000 79** **** 6361"),  # Маскирование корректного типа карты
        ("Счт 73654108430135874305", ValueError),  # Некорректные данные
    ],
)
def test_mask_account_card(input_data: str, expected_output: str) -> None:
    if expected_output == ValueError:
        with pytest.raises(ValueError):
            mask_account_card(input_data)
    else:
        result = mask_account_card(input_data)
        assert result == expected_output


# Параметризация теста даты
@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),  # преобразование даты
        ("2023-12-31T23:59:59.999999", "31.12.2023"),  # Последний день года
        ("2024-01-01T00:00:00.000000", "01.01.2024"),  # Первый день года
        ("", None),  # Пустая дата
    ],
)
def test_get_date(input_data: str, expected_output: str) -> None:
    if input_data:  # Проверка, что строка не пустая (truthy style)
        result = get_date(input_data)
        assert result == expected_output
    else:
        # Ожидаем ошибку ValueError для пустой строки
        with pytest.raises(ValueError):
            get_date(input_data)
