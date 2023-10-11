"""
Напишите функцию, которая принимает два списка и возвращает все целочисленные элементы первого и второго списка
в порядке убывания
"""


def get_numbers(a: list, b: list) -> list | None:
    """
    Функция которая возвращает все целочисленные элементы первого и второго списка в порядке убывания
    :param a: первый список
    :param b: второй список
    :return:
        list: возвращает список если в обоих списках есть целочисленные элементы
        None: возвращает None если в обоих списках нет целочисленных элементов
    """
    a.extend(b)
    c = [int(elem) for elem in a if str(elem).isnumeric()]
    c.sort()
    if len(c):
        return c
    else:
        return None
