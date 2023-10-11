"""
Напишите функцию, которая принимает два списка и возвращает все целочисленные элементы первого и второго списка
в порядке убывания
"""


def get_numbers(a: list, b: list) -> list | None:
    a.extend(b)
    c = []
    for elem in a:
        if str(elem).isnumeric():
            c.append(int(elem))
    if len(a):
        return c
    else:
        return None


if __name__ == "__main__":
    main()

