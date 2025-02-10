from typing import Any, Dict, Iterator, List


def filter_by_currency(info: List[Dict], usd: str) -> Iterator[int]:
    """Выдает по очереди операции, в которых указана заданная валюта."""
    for key in info:
        if key["operationAmount"]["currency"].get("code") == usd:
            yield key


def transaction_descriptions(info: List[dict]) -> Iterator[Any]:
    """Принимает список словарей и возвращает описание каждой операции по очереди."""
    for val in info:
        yield val.get("description")


def card_number_generator(start: int, stop: int):
    """Генератор номеров банковских карт"""
    for card_list in range(start, stop + 1):
        if 1 <= start <= 9999999999999999 or 1 <= stop <= 9999999999999999:
            number = "".join([f"{card_list:016}" for _ in range(16)])
            formatted_card_number = " ".join([number[i : i + 4] for i in range(0, 16, 4)])
            yield formatted_card_number
