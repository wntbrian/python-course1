"""
*Для самых смелых.
Написать консольную утилиту, передав которому путь к какой то папке,
она выводит список файлов и папок, которые есть в этой папке.
Используя библиотеки os и sys
"""
from os import listdir
from os.path import isfile, join
from sys import exit, argv

DIRNAME="./"


def ls_directory(path,move):
    try:
        dirs=listdir(path)
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

        if isfile(join(path, obj)):
            print("{}{}--{}".format(move, stage, obj))
        else:
            #move = move[:len(move) - 1] + move[len(move) - 1].replace("|", " ") + move[len(move):]
            print("{}{}--{}".format(move, stage, obj))
            if stage == "`":
                last = " "
            else:
                last = "|"
            ls_directory(join(path, obj), move+"{}   ".format(last))

if (len(argv)>1):
    DIRNAME=argv[1]
print(DIRNAME)
ls_directory(DIRNAME, "")