from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """
    Функция обрабатывает информацию о картах и о счетах

    Parameters:
      - account_card (str): тип и номер карты или счета.
    Примеры:
      - Visa Platinum 7000792289606361
      - Счет 73654108430135874305

    Returns:
      - (str): Замаскированный номер карты или счета.
    Примеры:
      - Visa Platinum 7000 79** **** 6361
      - Счет **4305
    """
    masked_account_card = ""

    # расщепляем строку на две — по первому пробелу с конца
    account_type, account_number = account_card.rsplit(" ", 1)

    if account_type == "Счет":
        masked_account_card = f"{account_type} {get_mask_account(account_number)}"
    else:
        masked_account_card = f"{account_type} {get_mask_card_number(account_number)}"

    return masked_account_card


def get_date(date_long: str) -> str:
    """
    Функция форматирует строку с датой формата "ГГГГ-ММ-ДДTЧЧ:ММ:СС.МС" в формат "ДД.ММ.ГГГГ".

    Parameters:
      - date_long (str): строка с длинным форматом даты и времени в ISO8601. Примеры: "2024-03-11T02:26:18.671407".

    Returns:
      - date_short (str): короткий формат — только дата. Примеры: "11.03.2024".
    """
    # Парсим строку даты в объект datetime
    datetime_object = datetime.strptime(date_long, "%Y-%m-%dT%H:%M:%S.%f")

    # Форматируем объект datetime в короткий формат
    date_short = datetime_object.strftime("%d.%m.%Y")

    return date_short
