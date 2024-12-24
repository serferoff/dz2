from datetime import datetime

def filter_by_state(transactions, state='EXECUTED'):
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param transactions: Список словарей с транзакциями.
    :param state: Значение ключа 'state' для фильтрации (по умолчанию 'EXECUTED').
    :return: Новый список словарей, содержащий только те, у которых ключ 'state' соответствует указанному значению.
    """
    return [transaction for transaction in transactions if transaction.get('state') == state]

def sort_by_date(transactions, descending=True):
    """
    Сортирует список словарей по дате.

    :param transactions: Список словарей с транзакциями.
    :param descending: Порядок сортировки (по умолчанию - True для убывания).
    :return: Новый отсортированный список словарей по дате.
    """
    return sorted(transactions, key=lambda x: datetime.fromisoformat(x['date']), reverse=descending)