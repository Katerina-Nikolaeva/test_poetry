def get_mask_card_number(card_number: str) -> str:
    """
    Функция маскировки номера банковской карты.

    Parameters:
      - card_number (str): Номер банковской карты.
    Примеры:
      - 7000792289606361

    Returns:
      - (str): Замаскированный номер карты, разделенный на блоки по 4 цифры.
    Пример:
      - 7000 79** **** 6361
    """
    if len(card_number) == 16:
        card_number_masked_chars = list(card_number)
        # Маскируем символы с 7 по 12 включительно
        for index in range(len(card_number)):
            if index in range(6, 12):
                card_number_masked_chars[index] = "*"
            else:
                card_number_masked_chars[index] = card_number[index]
        card_number_masked = "".join(card_number_masked_chars)
        # Разбиваем на части по 4 символа в каждой и добавляем между ними пробелы
        card_number_masked = " ".join(
            [card_number_masked[0:4], card_number_masked[4:8], card_number_masked[8:12], card_number_masked[12:16]]
        )
        return card_number_masked
    else:
        return ""


def get_mask_account(account_number: str) -> str:
    """
    Функция маскировки номера банковского счета.

    Parameters:
      - account_number (str): Номер банковского счета.
    Примеры:
      - 73654108430135874305

    Returns:
      (str): Замаскированный номер банковского счета.
    Примеры:
      - **4305
    """
    # Берём последние 4 цифры номера счёта
    last_four_digits = account_number[-4:]

    # Создаём маску в формате "**XXXX"
    masked_account = f"**{last_four_digits}"

    return masked_account
