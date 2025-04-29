import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_mask_card(testing_masks):
    assert get_mask_card_number(testing_masks) == "Maestro 1596 83** **** 5199"

    assert get_mask_card_number([]) == "Ошибка, проверьте правильность ввода."

    assert get_mask_card_number("") == "Ошибка, проверьте правильность ввода."

    with pytest.raises(TypeError):
        assert get_mask_card_number(1) == "Ошибка, проверьте правильность ввода."


def test_account(testing_card_number):
    assert get_mask_account(testing_card_number) == "Счет **4305"

    assert get_mask_account("") == "Ошибка, проверьте правильность ввода."


@pytest.mark.parametrize(
    "inter, out",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 934934", "Ошибка, проверьте правильность ввода."),
        ("", "Ошибка, проверьте правильность ввода."),
    ],
)
def test_account_par(inter, out):
    assert get_mask_account(inter) == out
