import os


from src.utils import read_file_json, read_file_csv, read_file_excel
from config import ROOT_DIR


def test_read_file():
    """Тестирует функцию открытия и считывания JSON файла"""
    assert read_file_json() == []
    assert read_file_json(str([])) == []
    assert read_file_json("") == []
    assert read_file_json("../data/operations.json")[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


def test_read_file_csv():
    """Тестирует функцию открытия и считывания CVS файла"""
    csv_path = os.path.join(ROOT_DIR, 'data', 'transactions.csv')
    assert read_file_csv() == []
    assert read_file_csv(str([])) == []
    assert read_file_csv("") == []
    assert read_file_csv(csv_path)[0] == {
        "id": "650703",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": "16210",
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }


def test_read_file_excel():
    """Тестирует функцию открытия и считывания EXCEL файла"""
    xlsx_path = os.path.join(ROOT_DIR, 'data', 'transactions_excel.xlsx')
    assert read_file_excel() == []
    assert read_file_excel(str([])) == []
    assert read_file_excel("") == []
    assert read_file_excel(xlsx_path)[0] == {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210.0,
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }
