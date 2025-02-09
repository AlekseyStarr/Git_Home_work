from typing import Any


def filter_by_state(transactions: list[dict[str, Any]], state_id: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция которая принимает список словарей и опционально значение для ключа state
    и возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению"""

    list_state = []

    for key in transactions:  # пройтись по списку и словарей
        if key.get("state") == state_id:  # возвращаем значение для указанного ключа
            list_state.append(key)
    return list_state


def sort_by_date(lists: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция возвращает новый список, отсортированный по дате"""

    sorted_inform_state = sorted(lists, key=lambda x: x["date"], reverse=reverse)
    return sorted_inform_state
