from datetime import datetime


def filter_by_state(items: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param items: список словарей с данными
    :param state: значение для фильтрации (по умолчанию 'EXECUTED')
    :return: новый список словарей, соответствующих указанному состоянию
    """
    filtered = []
    for item in items:
        if item.get("state") == state:
            filtered.append(item)
    return filtered


def sort_by_date(items: list[dict], descending: bool = True) -> list[dict]:
    """
    Сортирует список словарей по ключу 'date'.

    :param items: список словарей
    :param descending: порядок сортировки (True — по убыванию, False — по возрастанию)
    :return: новый список словарей, отсортированный по дате
    """
    return sorted(
        items,
        key=lambda x: datetime.fromisoformat(x["date"]),
        reverse=descending
    )