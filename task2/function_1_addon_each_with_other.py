'''
1. Даны четыре действительных числа: x1, y1, x2, y2.
Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2).
Считайте четыре действительных числа и выведите результат работы этой функции.

Реализуй функцию, которая считает не для двух точек, а для любого количества точек и выдает суммарное расстояние между ними
'''
from math import sqrt
def distance(args):
    dist = float()
    coord = list()
    for x1,y1 in zip(args[0::2],args[1::2]):
        coord.append((x1,y1))
    for j,elem in enumerate(coord):
        if j == len(coord) - 1:
            break
        for coo in coord[j+1:]:
            dist+=sqrt((abs(elem[0]**2-coo[0]**2))+(abs(elem[1]**2-coo[1]**2)))
    return dist
a = tuple(int(i) for i in input("Введите (x1 y1 x2 y2...), через пробел: ").split())
print("%.4f" % distance(a))