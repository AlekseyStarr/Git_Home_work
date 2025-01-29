from typing import Union
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../masks.log')
file_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: Union[str]) -> str | None:
    """Возвращает замаскированный номер карты в виде строки"""
    logger.info("Начали маскировку карты")
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[0:-12]} {card_number[-12:-10]}{"*" * 2} {"*" * 4} {card_number[-4:]}"
    else:
        logger.info("Окончили маскировку карты")
        return "Ошибка, проверьте правильность ввода"


def get_mask_account(acc_number: Union[str]) -> str | None:
    """Возвращает замаскированный номер учетной записи в виде строки"""
    logger.info("Начали маскировку номера счета")
    if acc_number.isdigit() and len(acc_number) == 20:
        return f"{'*' * 2}{acc_number[-4::]}"
    else:
        logger.info("Окончили маскировку номера счета")
        return "Ошибка, проверьте правильность ввода"
