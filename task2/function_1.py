'''
1. Даны четыре действительных числа: x1, y1, x2, y2.
Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2).
Считайте четыре действительных числа и выведите результат работы этой функции.
'''
from math import sqrt
def distance(x1, y1, x2, y2):
    a=x1**2-x2**2
    b=y1**2-y2**2
    dist=sqrt((abs(x1**2-x2**2))+(abs(y1**2-y2**2)))
    return dist
x1,y1,x2,y2 = map(float, input("Введите x1 y1 x2 y2, через пробел: ").split())
print("%.4f" % distance(x1,y1,x2,y2))