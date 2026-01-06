from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

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
