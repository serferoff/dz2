mkdir src
touch src/widget.py
def mask_account_card(info):
    # Разделяем строку на тип и номер
    card_type, card_number = info.rsplit(' ', 1)

    # Маскировка для карт
    if 'Счет' not in card_type:
        masked_number = card_number[:4] + ' ' + card_number[4:6] + '** **** ' + card_number[-4:]
    # Маскировка для счетов
    else:
        masked_number = card_type + ' **' + card_number[-4:]

    return f"{card_type} {masked_number}"

from datetime import datetime

def get_date(date_str):
    # Преобразуем строку в объект datetime и форматируем его
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")