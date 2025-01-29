import json
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("../utils.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_file_json(filename: str = None) -> list:
    """Функция принимающая путь к файлу, считывает информацию c JSON файла"""
    try:
        """Это логер для функции read_file"""
        logger.info("Начал выгрузку с файла JSON формата")
        with open(filename, encoding="utf-8") as file:  # Открытие и считывание файла формата JSON
            reading = json.load(file)  # Преобразование JSON файла в пайтон обьект
            logger.info("Оконили выгрузку с файла JSON формата")
        return reading
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
        return []  # В случае ошибки возвращает пустой список
