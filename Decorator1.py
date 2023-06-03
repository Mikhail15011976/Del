#Доработать параметризованный декоратор logger в коде ниже. Должен получиться декоратор, который записывает
# в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась, и возвращаемое значение.
# Путь к файлу должен передаваться в аргументах декоратора. Функция test_2 в коде ниже также должна отработать
# без ошибок.

import os

def logger(old_function):
    def new_function(*args, **kwargs):

        import datetime
        with open('main.log', 'a', encoding='utf-8') as f:

            datetime = datetime.datetime.now()
            f.write(f'Дата и время вызова функции {datetime}\n')
            f.write(f'Имя функции {old_function}\n')
            for arg in args:
                f.write(f'Данные args {arg}\n')
            for kwarg in kwargs:
                f.write(f'Данные kwargs {kwarg}\n')
            result = old_function(*args, **kwargs)
            f.write(f'Возвращаемое значение функции {result}\n')

        return result

    return new_function


def test_1():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()