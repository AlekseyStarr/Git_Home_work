import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_mask_card(testing_masks):
    assert get_mask_card_number(testing_masks) == "1596 83** **** 5199"
    assert get_mask_card_number("") == "Ошибка, проверьте правильность ввода"


def test_account(testing_card_number):
    assert get_mask_account(testing_card_number) == "**4305"
    assert get_mask_account("") == "Ошибка, проверьте правильность ввода"


@pytest.mark.parametrize(
    "inter, out",
    [
        ("73654108430135874305", "**4305"),
        ("", "Ошибка, проверьте правильность ввода"),
    ],
)
def test_account_par(inter, out):
    assert get_mask_account(inter) == out
