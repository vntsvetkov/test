"""
Напишите программу, которая принимает имя файла с расширением и возвращает его имя в перевернутом виде.
"""


def reverse_name_file(name_file: str) -> str:
    if name_file. count(".") > 1:
        return "Имя файла введено некорректно"
    elif name_file.count(".") == 0:
        return "У данного файла не расширения"
    else:
        index = name_file.find(".")
        revers_name = name_file[index - 1:: -1] + name_file[index:]
        return revers_name
