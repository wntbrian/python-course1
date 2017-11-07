"""
1.Дан файл с пунктами меню (id, название, id родителя). Если id родителя равно 0, то родителя не существует.
Показать полное меню с отступами. Пользователь вводит id пункта.
Показать цепочку из пунктов меню до этого пункта. Уровней вложенности в меню может быть любое количество.
"""


import os
import sys


def read_file_form_path(filename):
    strings = list()
    try:
        with open(filename, 'r') as file:
            strings = file.readlines()
    except FileNotFoundError:
        filepath = os.path.dirname(os.path.realpath(__file__))
        print("Файл {} не найден, создайте файл и запустите скрипт заново."
              .format(os.path.join(filepath, filename)))
        sys.exit(0)
    return strings


def get_menu_items(lst):
    import re
    result = list()
    for string in lst:
        raw_menu = list(filter(None, re.split(' *, *', string.strip())))
        result.append(raw_menu)
    return result


def user_menu(arr,addr):
    print("Схема до найденого пункта меню:")
    move = ""
    for x in addr:
        print("{}`-- {}".format(move,arr[x][-1]))
        move += "   "
        arr = arr[x]


def show_menu(result, list_menu, limit='', addr=list(), pid='0', level=0):
    global address
    j = c = 0

    for e in list_menu:
        if e[2] == pid:
            c = c + 1

    for elem in list_menu:
        if elem[2] == pid:
            space = ""
            for i in range(level):
                if print_list[i] == 1:
                    space += "| "
                else:
                    space += "  "
            if j == (c - 1):
                print("{}`-- {}".format(space, elem[1]))
                print_list.insert(level, 0)
            else:
                print("{}|-- {}".format(space, elem[1]))
                print_list.insert(level, 1)
            result.insert(j,elem[1:-1])
            addr.insert(level, j)
            if elem[0] == limit:
                address = addr[:level + 1]
            j = j + 1
            show_menu(result[j-1], list_menu, limit, addr, elem[0], level + 1)


print_list = list()
menu = list()
address = list()

data = read_file_form_path('menu')
items = get_menu_items(data)
menuid = input("Ввелите ID требуемого меню: ")
print("Меню для поиска: ")
show_menu(menu, items, menuid)
user_menu(menu, address)