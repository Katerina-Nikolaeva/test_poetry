from src.masks import get_mask_account, get_mask_card_number

if __name__ == "__main__":
    card_number = "7000792289606361"
    print(f"-> card number:        {card_number}")
    card_number_masked = get_mask_card_number(card_number)
    print(f"-> card number masked: {card_number_masked}")

    account = "73654108430135874305"
    print(f"-> account: {account}")
    mask_account = get_mask_account(account)
    print(f"-> masked account: {mask_account}")
