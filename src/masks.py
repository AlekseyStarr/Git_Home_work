import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("../masks.log")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(number: str) -> str:
    """Маскирует номер карты"""
    logger.info("Начали маскировку карты")
    if len(number) < 16 or isinstance(number, int):
        return "Ошибка, проверьте правильность ввода."
    else:
        mask_number = number[0:-12] + " " + number[-12:-10] + 2 * "*" + " " + 4 * "*" + " " + number[-4:]
    logger.info("Окончили маскировку карты")
    return mask_number


def get_mask_account(account: str) -> str:
    """Маскирует номер счета"""
    """Это логер для функции get_mask_account"""
    logger.info("Начали маскировку номера счета")
    inter = str(account)
    if len(account) < 20:
        return "Ошибка, проверьте правильность ввода."
    else:
        account = "Счет " + 2 * "*" + inter[-4:]
        logger.info("Окончили маскировку номера счета")
    return account
