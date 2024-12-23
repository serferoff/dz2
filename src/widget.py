from src.masks import get_mask_card_number, get_mask_account
from datetime import datetime


def mask_account_card(info: str) -> str:
    """
    Функция для маскировки номера карты или счета на основе предоставленной информации.
    Проверяет входные данные и использует функции маскировки из модуля masks.py.

    :param info: str, строка в формате "Тип Номер"
    :return: str, строка с маскированным номером
    :raises ValueError: если номер карты или счета некорректный
    """
    # Разделяем строку на тип и номер
    parts = info.rsplit(' ', 1)
    if len(parts) != 2:
        raise ValueError("Информация должна содержать тип и номер, разделенные пробелом.")

    card_type: str = parts[0]
    card_number: str = parts[1]

    # Проверка входных данных
    if 'Счет' not in card_type and len(card_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр.")
    if 'Счет' in card_type and len(card_number) != 20:
        raise ValueError("Номер счета должен содержать 20 цифр.")

    # Маскировка для карт
    if 'Счет' not in card_type:
        masked_number: str = get_mask_card_number(card_number)
    # Маскировка для счетов
    else:
        masked_number = get_mask_account(card_number)

    return f"{card_type} {masked_number}"


def get_date(date_str: str) -> str:
    """
    Преобразует строку в формат даты.

    :param date_str: str, строка с датой в формате ISO
    :return: str, дата в формате "дд.мм.гггг"
    """
    # Преобразуем строку в объект datetime и форматируем его
    date_obj: datetime = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")
