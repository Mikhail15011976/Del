#Применить написанный логгер к приложению из любого предыдущего д/з.

import os
import types

def logger(old_function):
    def new_function(*args, **kwargs):

        import datetime
        with open('generator.log', 'w', encoding='utf-8') as f:

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

@logger
def Flat_generator(list_of_list):
    for i in list_of_list:
        for j in i:
            yield j

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            Flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(Flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(Flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()