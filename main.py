from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card
from src.processing import filter_by_state, sort_by_date

if __name__ == "__main__":
    card_number = "7000792289606361"
    print(f"-> card number:        {card_number}")
    card_number_masked = get_mask_card_number(card_number)
    print(f"-> card number masked: {card_number_masked}")

    account = "73654108430135874305"
    print(f"-> account: {account}")
    mask_account = get_mask_account(account)
    print(f"-> masked account: {mask_account}")

    account_data = "Счет 73654108430135874305"
    print(f"-> account data: {account_data}")
    mask_account_data = mask_account_card(account_data)
    print(f"-> masked account data: {mask_account_data}")

    account_data = "Visa Platinum 7000792289606361"
    print(f"-> account data: {account_data}")
    mask_account_data = mask_account_card(account_data)
    print(f"-> masked account data: {mask_account_data}")

    date_long = "2024-03-11T02:26:18.671407"
    print(f"-> account data: {date_long}")
    date_short = get_date(date_long)
    print(f"-> masked account data: {date_short}")

    dict_data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                 {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    state = 'CANCELED'
    filtered_data = filter_by_state(dict_data,state)
    print(f"-> filtered data: {filtered_data}")


    data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                 {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    order ='descending'
    sorted_data = sort_by_date(data,order)
    print(f"-> sorted data: {sorted_data}")
