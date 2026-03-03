import json


def load_file_list(file_path):
    """
    Читает JSON-файл с финансовыми транзакциями и возвращает список словарей.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.

    :param file_path: Путь до JSON-файла с транзакциями
    :return: Список словарей с информацией о транзакциях или пустой список
    """
    try:
        # Открываем файл и загружаем его содержимое
        with open(file_path, mode="r", encoding="utf-8") as file:
            transactions = json.load(file)

        # Проверяем, что загруженный объект действительно список
        if isinstance(transactions, list):
            return transactions
        else:
            return []  # Возвращаем пустой список, если структура неверная
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Возврат пустого списка в случае отсутствия файла или ошибки формата JSON
