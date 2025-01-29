from src.widget import get_data, mask_account_card


user_input = input("Введите данные счета или карты: ")
masked_output = (mask_account_card(user_input))
print(masked_output)

print(get_data("2024-03-11T02:26:18.671407"))
