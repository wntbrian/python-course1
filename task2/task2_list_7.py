'''
Даны два списка произвольной длины каждый. Списки могут содержать как числа, так и строки.
Необходимо вывести только те элементы, которые входят как первый список, так и во второй.
'''
def list7(list1,list2):
    res = set()
    for lst in list1:
         if lst in list2:
              res.add(lst)
    if (len(res)):
        return res
    else:
        return False
list1 = input("Введите первый список, элементы разделите пробелом: ").split()
list2 = input("Введите второй список, элементы разделите пробелом: ").split()
print(list7(list1, list2))
