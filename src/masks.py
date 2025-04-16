def get_mask_card_number(card_number: str) -> str:
    """функция маскировки номера карты"""

    return card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]

def get_mask_account(account_number: str) -> str:
    """функция маскировки номера аккаунта"""
    return "**" + account_number[-4:]
