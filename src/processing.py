from typing import Any

word = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def filter_by_state(words: list[dict[str, Any]], state_id: str = "EXECUTED") -> list[dict[str, Any]]:
    '''Функция которая принимает список словарей и опционально значение для ключа state
        и возвращает новый список словарей, содержащий только те словари, у которых ключ state
        соответствует указанному значению'''

    list_state = []

    for key in words:                    # пройтись по списку и словарей
        if key.get("state") == state_id: # возвращаем значение для указанного ключа
            list_state.append(key)
    return list_state



def sort_by_date(words: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    '''Функция возвращает новый список, отсортированный по дате'''

    sorted_inform_state = sorted(words, key=lambda x: x["date"], reverse=reverse)
    return sorted_inform_state


print(filter_by_state(word))
print(sort_by_date(word))
