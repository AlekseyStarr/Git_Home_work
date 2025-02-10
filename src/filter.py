import re
from collections import Counter


def filter_word(list_filter: list, option: str) -> list:
    """Функция фильтрует список по заданному значению в описании"""
    new_list_filter = []
    for i in list_filter:
        if "description" in i and re.search(option, i["description"], flags=re.IGNORECASE):
            new_list_filter.append(i)
    return new_list_filter


def filter_category(list_filter: list, list_category: list) -> dict:
    """Функция фильтрует список по категориям и возвращает количество операция по категориям"""
    new_list = []
    for i in list_filter:
        if "description" in i:
            if i["description"] in list_category:
                new_list.append(i["description"])
    counted = Counter(new_list)
    return counted
