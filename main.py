import os.path
import re

from src.filter import filter_word
from src.processing import filter_by_state, sort_by_date
from src.utils import read_file_csv, read_file_excel, read_file_json
from src.widget import get_data, mask_account_card


def main():
    work_file = input(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями. "
        "\nВыберите необходимый пункт меню: "
        "\n1.Получить информацию о транзакциях из JSON-файла"
        "\n2.Получить информацию о транзакциях из CSV-файла"
        "\n3.Получить информацию о транзакциях из XLSX-файла"
        "\nВвод: ").strip()
    while True:
        if work_file == "1":
            print("Для обработки выбран JSON-файл")
            read_file = read_file_json(os.path.join(os.path.dirname(__file__), "data/operations.json"))
            break
        elif work_file == "2":
            print("Для обработки выбран CSV-файл")
            read_file = read_file_csv(os.path.join(os.path.dirname(__file__), "data/transactions.csv"))
            break
        elif work_file == "3":
            print("Для обработки выбран XLSX-файл")
            read_file = read_file_excel(os.path.join(os.path.dirname(__file__), "data/transactions_excel.xlsx"))
            break
        else:
            work_file = input("Данного варианта нет в списке, попробуйте еще раз:\nВвод: ")

    status_operation = input("\nВведите статус, по которому необходимо выполнить фильтрацию. "
                             "\nДоступные для фильтровки статусы: "
                             "EXECUTED, CANCELED, PENDING:\nВвод: ").strip().upper()

    while True:
        if status_operation == "PENDING" or status_operation == "EXECUTED" or status_operation == "CANCELED":
            status_operation_filter = filter_by_state(read_file, status_operation)  # ДЕЙСТВУЮЩИЙ ФИЛЬРУЕМЫЙ СПИСОК
            break
        else:
            status_operation = input(f"Статус {status_operation} не доступен.\n"
                                     "\nВведите статус, по которому необходимо выполнить фильтрацию."
                                     "\nДоступные для фильтровки статусы: "
                                     "EXECUTED, CANCELED, PENDING:\nВвод: ").strip().upper()

    while True:
        question_sort_data = input("Отсортировать операции по дате? Да/Нет\nВвод: ").lower()
        if question_sort_data == "да":
            question_sort_data_reverse = input("Отсортировать по возрастанию или по убыванию?\nВвод: ")
            sort_data_reverse = re.search("убыванию", question_sort_data_reverse)
            sort_data_status_operation = sort_by_date(status_operation_filter, sort_data_reverse)
            print(sort_data_status_operation) # тест сортировки по убыванию
            break
        elif question_sort_data == "нет":
            sort_data_status_operation = status_operation_filter
            break
        else:
            print("Данного варианта нет в списке, попробуйте еще раз:")
            continue

    while True:
        question_currency = input("Выводить только рублевые транзакции? Да/Нет\nВвод: ").lower()
        if question_currency == "да":
            new_list_sort = []
            for i in sort_data_status_operation:
                if i["currency_code"] == "RUB":
                    new_list_sort.append(i)
            print(new_list_sort) #тест фильтрации рублевого счета
            break
        elif question_currency == "нет":
            new_list_sort = sort_data_status_operation
            break
        else:
            print("Данного варианта нет в списке, попробуйте еще раз: ")
            continue

    while True:
        question_description = input(
            "Отфильтровать список транзакций по определенному слову описании? Да/Нет\nВвод: ").lower()
        if question_description == "да":
            question_description_word = input("Введите слово: ")
            finaly_filter = filter_word(new_list_sort, question_description_word)
            print(finaly_filter) # тест фильтрации по слову
            break
        elif question_description == "нет":
            finaly_filter = new_list_sort
            break
        else:
            print("Данного варианта нет в списке, попробуйте еще раз: ")
            continue

    print(f"Распечатываю итоговый список транзакций...\nВсего банковских операций в выборке: {len(finaly_filter)}\n")
    if len(finaly_filter) == 0:
        for trans in finaly_filter:
            if trans["description"] in "Открытие вклада" in trans["description"]:
                print(f"{get_data(trans["date"])} Открытие вклада\n{mask_account_card(trans["to"])}"
                  f"\nСумма:{trans["amount"]}\n")
            else:
                print(f"{get_data(trans["date"])} {trans["description"]}\n{mask_account_card(trans["from"])} -> "
                      f"{mask_account_card(trans["to"])}\nСумма: {trans["amount"]} {trans["currency_code"]}\n")
        else:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

if __name__ == '__main__':
    main()
