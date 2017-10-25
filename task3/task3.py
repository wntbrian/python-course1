"""
2. В одном файле в каждой строке записаны координаты пар точек.
Каждая координата отделена от другой пробелом.
Например, строка вида 3 6 -2 4 означает,
что координаты первой точки (3;6),
второй - (-2;4).
Во второй файл требуется построчно записать наибольшее
и наименьшее расстояние между точками.

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
import os


FILENAME_INPUT="input"
FILENAME_OUTPUT="output"


def read_file_form_path(self):
    try:
        file = open(self,'r')
    except FileNotFoundError:
        print("Файл {} не найден, создайте фаил и запустите скрипт заного."
              .format(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                   self)))
        close_application()
    strings = file.readlines()
    return strings


def close_application():
    import sys
    sys.exit(0)


def calc_distance(self):
    distance = list()
    from math import sqrt
    for coord in self:
        distance.append(sqrt((abs(coord[0]**2-coord[2]**2))
                             + abs((coord[1]**2-coord[3]**2))))
    return distance


def find_max_min(self):
    self.sort()
    return [self[0], self[-1]]


def write_to_file(self, lst):
    with open(self,'w') as file:
        if (lst[0] == lst[1]):
            file.writelines('{}'.format(lst[0]))
        else:
            file.writelines('{},{}'.format(lst[0],lst[1]))


def get_coordinates_from_list(self):
    result = list()
    for coord in self:
        try:
            x1, y1, x2, y2 = map(float,coord[:-1].split())
            result.append([x1, y1, x2, y2])
        except ValueError:
            print("Сторока с координатами {} имеет не допустимый формат. "
                  "Точка иключается из подсчета.".format(coord[:-1]))
    return result


write_to_file(FILENAME_OUTPUT,
              find_max_min(calc_distance(get_coordinates_from_list(read_file_form_path(FILENAME_INPUT)))))

#print(calc_distance(a))
#print (read_file_form_path("./input"))