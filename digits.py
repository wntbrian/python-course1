###
### Задание 1, Вариант 2, Числа №2
###
def NeededDesk(numbers):
    desk=0
    for num in numbers:
        desk += int(num) // 2 + int(num) % 2
    return str(desk);
input=input("Кол-во учеников в каждом классе через пробел: ")

print("Для учеников потребуется: "+ NeededDesk(input.split( ))+" новых парт")