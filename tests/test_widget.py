import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("inter, out",
         [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
         ("Счет 73654108430135874305", "Счет **4305")],)


def test_mask_account(inter, out):
    assert mask_account_card(inter) == out


@pytest.mark.parametrize("data_test, correct_data",
         [("2024-03-11T02:26:18.671407", "11.03.2024")])

def test_get_date(data_test, correct_data):
    assert get_date(data_test) == correct_data
