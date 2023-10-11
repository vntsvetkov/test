"""
Напишите программу, которая принимает имя файла с расширением и возвращает его имя в перевернутом виде.
"""


def reverse_name_file(name_file: str) -> str:
    index = name_file.find(".")
    revers_name = name_file[index - 1:: -1] + name_file[index:]
    return revers_name
