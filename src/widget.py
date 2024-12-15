from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number_account_card: str) -> str:
    """Функция, которая маскирует номер счета или карты"""

    parts = number_account_card.split(" ")  # Дробим строку на части по пробелу
    identifier = " ".join(parts[:-1])  # До -1 элемента это название, соединяем
    number = parts[-1]  # а -1 номер, Берем в переменную для удобства

    if len(number) == 16:
        return f"{identifier} {get_mask_card_number(number)}"
    else:
        return f"{identifier} {get_mask_account(number)}"


def get_date(user_data: Union[str]) -> str:
    """Функция, которая изменяет формат даты"""
    data_day = user_data.split("Т")[0]

    return f"{(user_data[8:10])}.{(data_day.split('-')[-2])}.{(data_day.split('-')[-3])}"
