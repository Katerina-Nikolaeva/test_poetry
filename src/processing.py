def filter_by_state (dict_data, state: 'EXECUTED'):
    """
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state = EXECUTED

    Parameters:
      - dict_data: список словарей
      - state: str = 'EXECUTED'
    Примеры:
      - {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}

    Returns:
      - Отфильтрованный список словарей
    Пример:
      - [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
      - [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}
    """
    filtered_data = []
    for item in dict_data:
        if item.get('state') == state:
           filtered_data.append(item)
    return filtered_data



