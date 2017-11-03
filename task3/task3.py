"""
2. В одном файле в каждой строке записаны координаты пар точек.
Каждая координата отделена от другой пробелом.
Например, строка вида 3 6 -2 4 означает,
что координаты первой точки (3;6),
второй - (-2;4).
Во второй файл требуется построчно записать наибольшее
и наименьшее расстояние между точками.
"""
import os


FILENAME_INPUT="input"
FILENAME_OUTPUT="output"


def read_file_form_path(filename):
    strings = list()
    try:
        with open(filename, 'r') as file:
            strings = file.readlines()
    except FileNotFoundError:
        filepath = os.path.dirname(os.path.realpath(__file__))
        print("Файл {} не найден, создайте файл и запустите скрипт заново."
              .format(os.path.join(filepath, filename)))
        close_application()
    return strings


def close_application():
    import sys
    sys.exit(0)


def calc_distance(coords):
    distance = list()
    from math import sqrt
    for coord in coords:
        try:
            distance.append(sqrt((coord[2]-coord[0])**2+(coord[3]-coord[1])**2))
        except IndexError:
            print("Сторока с координатами {} имеет не допустимый формат. "
                  "Точка иключается из подсчета.".format(coord))
    return distance


def find_max_min(coords):
    try:
        return [min(coords),max(coords)]
    except ValueError:
        print("Не достаточно точек. Расстояние - 0")
        return [0]


def write_to_file(filename, lst):
    try:
        with open(filename,'w') as file:
            if (len(lst) == 1 or lst[0] == lst[1]):
                file.writelines('{}'.format(lst[0]))
            else:
                file.writelines('{},{}'.format(lst[0],lst[1]))
    except FileNotFoundError:
        filepath = os.path.dirname(os.path.realpath(__file__))
        print("Не возможно создать файл {}. "
              .format(os.path.join(filepath, filename)))
        close_application()


def get_coordinates_from_list(lst):
    import re
    result = list()
    for str in lst:
        coord = list(filter(None,re.split('[^0-9.]+', str)))
        result.append([float(c) for c in coord])
    return result

coord_list = read_file_form_path(FILENAME_INPUT)
coords = get_coordinates_from_list(coord_list)
dist = calc_distance(coords)
result_distance = find_max_min(dist)
write_to_file(FILENAME_OUTPUT,result_distance)