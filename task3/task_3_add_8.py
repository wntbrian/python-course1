"""
Cоздать типизированный файл записей со сведениями о телефонах абонентов
каждая запись имеет поля:
фамилия абонента, год установки телефона, номер телефона.
По заданной фамилии абонента выдать номера его телефонов.
Определить количество установленных телефонов с N-го года.

*Для самых смелых.
Написать консольную утилиту, передав которому путь к какой то папке,
она выводит список файлов и папок, которые есть в этой папке.
Используя библиотеки os и sys
"""
#import os
#from os.path import isfile, join
from os import listdir
#mypath = os.path.dirname(os.path.realpath(__file__))


def ls_directory(path):
    return listdir(path)


def ls_files_only(path):
    from os.path import isfile, join
    return [f for f in listdir(path) if isfile(join(path, f))]


#onlyfiles = [f for f in os.listdir(mypath) if isfile(join(mypath, f))]
#import os
print (ls_directory('.'))
print (ls_files_only('.'))


#NotADirectoryError
#
