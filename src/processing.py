from datetime import datetime


def filter_by_state (dict_data, state: str = 'EXECUTED') -> list:
    """
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state = EXECUTED

    Parameters:
      - dict_data (list of dict): список словарей
      - state: str = 'EXECUTED'
    Примеры:
      - [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]

    Returns:
      - Отфильтрованный список словарей
    Пример:
      - [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
      - [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]
    """
    filtered_data = []
    for item in dict_data:
        if item.get('state') == state:
           filtered_data.append(item)
    return filtered_data

    # filtered_data = [item for item in dict_data if item.get('state') == state ]
    # return filtered_data

def sort_by_date (data, order: str ='descending')-> list:
    """
    Функция сортирует список словарей по дате (ключ 'date').

    Parameters:
      - data (list of dict): Список словарей для сортировки.
      - order (str, optional): Порядок сортировки ('ascending' или 'descending').
    Примеры:
      - [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]

    Returns:
      - sorted_data (list of dict): Отсортированный список словарей.

    Пример:
      - [
          {'id': 41428829,  'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
          {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
          {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        ]
    """
    sorted_data = sorted(
        data,
        key=lambda item: datetime.fromisoformat(item.get('date')),
        reverse=(order == 'descending')
    )
    return sorted_data