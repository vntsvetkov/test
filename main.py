"""
Напишите функцию, которая принимает два списка и возвращает все целочисленные элементы первого и второго списка
в порядке убывания
"""


def get_numbers(a: list, b: list) -> list | None:
    a.extend(b)
    c = [int(elem) for elem in a if str(elem).isnumeric()].sort()
    if len(a):
        return c
    else:
        return None


if __name__ == "__main__":
    get_numbers()

