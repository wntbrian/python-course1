"""
*Для самых смелых.
Написать консольную утилиту, передав которому путь к какой то папке,
она выводит список файлов и папок, которые есть в этой папке.
Используя библиотеки os и sys
"""
from os import listdir
from os.path import isfile, join


DIRNAME="./test"


def ls_directory(path,move):
    try:
        dirs=listdir(path)
    except NotADirectoryError:
        print("Данный путь - не директория.")
        import sys
        sys.exit(0)
    except FileNotFoundError:
        print("Такой директории не существует")
        import sys
        sys.exit(0)
    for idx,obj in enumerate(dirs):
        stage = "|"
        if idx == len(dirs)-1:
            stage = "`"
        if isfile(join(path, obj)):
            print("{}{}--{}".format(move, stage, obj))
        else:
            print("{}{}--{}".format(move, stage, obj))
            ls_directory(join(path, obj), move+"|   ")


print(DIRNAME)
ls_directory(DIRNAME,"")