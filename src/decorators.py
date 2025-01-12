from functools import wraps
from typing import Any


def log(filename: Any = None) -> Any:
    """Декоратор логирует вызов функций-обработчиков и результаты их работы"""

    def my_decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename is not None:
                    with open(filename, "w") as file:
                        file.write("my function OK")
                return result
            except Exception as e:
                if filename is not None:
                    with open(filename, "w") as file:
                        file.write(f"my function error:{e}. Input: {args, kwargs}")
                return func(*args, **kwargs)

        return wrapper

    return my_decorator


@log(filename="mylog.txt")
def my_function(x, y):
    """Функция для проверки работы декоратора"""
    return x / y


my_function(10, 2)
