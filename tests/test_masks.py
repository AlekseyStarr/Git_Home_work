import pytest

from src.widget import mask_account_card


def test_mask_card(testing_masks):
    assert mask_account_card(testing_masks) == "Maestro 1596 83** **** 5199"

    assert mask_account_card(str([])) == "Ошибка, проверьте правильность ввода."

    assert mask_account_card("") == "Ошибка, проверьте правильность ввода."

    with pytest.raises(TypeError):
        assert mask_account_card(1) == "Ошибка, проверьте правильность ввода."


def test_account(testing_card_number):
    assert mask_account_card(testing_card_number) == "Счет **4305"

    assert mask_account_card("") == "Ошибка, проверьте правильность ввода."


@pytest.mark.parametrize(
    "inter, out",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 934934", "Ошибка, проверьте правильность ввода."),
        ("", "Ошибка, проверьте правильность ввода."),
    ],
)
def test_account_par(inter, out):
    assert mask_account_card(inter) == out
