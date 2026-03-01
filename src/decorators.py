import functools
from datetime import datetime


def log(filename=None):
    """
    Декоратор, выполняющий журналирование (логирование) начала и конца выполнения функции,
    а также её результатов или возникающих ошибок.

    Параметры:
        filename (str, optional): Имя файла, в который будут записываться логи.
                                Если не указан (None), логи выводятся в консоль.

    Задача декоратора:
        1. Регистрация начала выполнения функции с указанием аргументов.
        2. Регистрация успешного завершения функции с результатами.
        3. Регистрация ошибок, если функция завершилась с исключением.

    Формат логов:
        - Дата и время начала выполнения функции.
        - Название функции, передаваемые аргументы (*args и **kwargs).
        - Дата и время завершения функции.
        - Результат выполнения функции (если завершился успешно).
        - Информация об ошибке (тип ошибки и детали), если функция вызвала исключение.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # Начало выполнения функции
                start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S,%f")
                log_message = f"{start_time} | {func.__name__}(*args={args}, **kwargs={kwargs}) STARTED\n"

                # Выполнение функции
                result = func(*args, **kwargs)

                # Успешное завершение
                finish_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S,%f")
                log_message += (
                    f"{finish_time} | {func.__name__}(*args={args}, **kwargs={kwargs}) FINISHED SUCCESSFULLY.\n"
                )
                log_message += f"{finish_time} | RESULT: {result}\n"

            except Exception as e:
                # Произошла ошибка
                finish_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S,%f")
                log_message += f"{finish_time} | {func.__name__}(*args={args}, **kwargs={kwargs}) ENDED WITH ERROR.\n"
                log_message += f"{finish_time} | TYPE OF ERROR: {type(e).__name__}.\n"
                log_message += f"{finish_time} | DETAILS: {str(e)}\n"
                raise  # поднимем исключение дальше по цепочке

            finally:
                # Запись логов
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message)
                else:
                    print(log_message)

            return result

        return wrapper

    return decorator
