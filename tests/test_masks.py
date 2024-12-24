import pytest

from src.masks import get_mask_account, get_mask_card_number


# Тест правильной маскировки номера карты
@pytest.mark.parametrize("card_number, expected",
                         [("1596837868705199", "1596 83** **** 5199")])


def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


# Тест правильной маскировки номера счета
@pytest.mark.parametrize("acc_number, expected",
                         [("73654108430135874305", "**4305")])


def test_get_mask_account(acc_number, expected):
    assert get_mask_account(acc_number) == expected
