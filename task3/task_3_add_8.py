"""
*Для самых смелых.
Написать консольную утилиту, передав которому путь к какой то папке,
она выводит список файлов и папок, которые есть в этой папке.
Используя библиотеки os и sys
"""
import os
from sys import exit, argv

DIRNAME="./"


def ls_directory(path,move):
    try:
        dirs=os.listdir(path)
    except NotADirectoryError:
        print("Данный путь - не директория.")
        exit(0)
    except FileNotFoundError:
        print("Такой директории не существует")
        exit(0)
    for idx,obj in enumerate(dirs):
        stage = "|"
        if idx == len(dirs)-1:
            stage = "`"

        if os.path.isfile(os.path.join(path, obj)):
            print("{}{}--{}".format(move, stage, obj))
        else:
            print("{}{}--{}".format(move, stage, obj))
            if stage == "`":
                last = " "
            else:
                last = "|"
            ls_directory(os.path.join(path, obj), move+"{}   ".format(last))

if (len(argv)>1):
    DIRNAME=argv[1]
print(DIRNAME)
ls_directory(DIRNAME, "")