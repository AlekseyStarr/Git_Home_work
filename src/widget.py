from typing import Union

def mask_account_card(type_and_number: str) -> str:
    """Функция, которая маскирует номер счета или карты"""
    if "Счёт" in type_and_number or "Счет" in type_and_number:
        return type_and_number[:4] + " " + "**" + type_and_number[-4:]
    else:
        return type_and_number[0:-12] + " " + type_and_number[-12:-10] + "** **** " + type_and_number[-4:]



def get_date(user_data: Union[str]) -> str:
    """Функция, которая изменяет формат даты"""
    data_day = user_data.split("Т")[0]

    return f"{(user_data[8:10])}.{(data_day.split('-')[-2])}.{(data_day.split('-')[-3])}"
