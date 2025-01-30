from src.widget import get_data, mask_account_card
from src.masks import get_mask_card_number
from src.utils import read_file_json


user_input = input("Введите данные счета или карты: ")
masked_output = (mask_account_card(user_input))
print(masked_output)

print(get_data("2024-03-11T02:26:18.671407"))
print(get_mask_card_number('1234567890123456'))
print(read_file_json('data/operations.json'))
