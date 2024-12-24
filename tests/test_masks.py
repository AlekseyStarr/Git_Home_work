import pytest

from src.masks import get_mask_account, get_mask_card_number


# Тест правильной маскировки номера карты
@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("159683786870519", "Ошибка, проверьте правильность ввода"),
        ("", "Ошибка, проверьте правильность ввода"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


# Тест правильной маскировки номера счета
@pytest.mark.parametrize(
    "acc_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("7365410843013587430", "Ошибка, проверьте правильность ввода"),
        ("", "Ошибка, проверьте правильность ввода"),
    ],
)
def test_get_mask_account(acc_number, expected):
    assert get_mask_account(acc_number) == expected
