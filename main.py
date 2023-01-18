'''1. Доработать класс FlatIterator в коде ниже.
Должен получиться итератор, который принимает список списков и возвращает их плоское представление,
т.е последовательность состоящую из вложенных элементов.
Функция test в коде ниже также должна отработать без ошибок.'''

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.new_list = []
        self.cursor = -1
        self.list_iter = iter(self.list_of_list)
        return self

    def __next__(self):
        self.cursor += 1
        if len(self.new_list) == self.cursor:
            self.new_list = None
            self.cursor = 0
            while not self.new_list:
                self.new_list = next(self.list_iter)
        return self.new_list[self.cursor]

def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
    list_of_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]
    for item in FlatIterator(list_of_list):
        print(item)
    flat_list = [item for item in FlatIterator(list_of_list)]
    print(flat_list)

'''2. Доработать функцию flat_generator, Должен получиться генератор, 
который принимает список списков и возвращает их плоское представление. 
Функция test в коде ниже также должна отработать без ошибок.'''

import types

def flat_generator(list_of_lists):
    for new_list in list_of_lists:
        for item in new_list:
            yield item

def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
    list_of_lists = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    for item in flat_generator(list_of_lists):
        print(item)
    flat_list_1 = [item for item in flat_generator(list_of_lists)]
    print(flat_list_1)