''' Задание 1, Вариант 2, Строки №6
Вам задана строка , состоящая из пробелов и латинских букв. Строка называется панграммой, если она содержит каждую из 26 латинских букв хотя бы раз. Определите является ли строка панграммой.
Формат входных данных
В единственной строке входных данных записана строка . Строка может содержать только пробелы, заглавные и строчные буквы латинского алфавита. Заглавные и строчные буквы считаются одинаковыми.
'''
def is_pangramma_ascii(str): #Функция поиска букв в строке, из плюсов не требует ничего делать с пробелами и лишними символами
    if len(str) >= 26:
        for i in range(26):
            if chr(ord('a') + i) not in str:
                return -1
            else:
                if i == 25:
                    return 1
        return -1
    else:
        return -1
input=input("Введите строку для проверки: ")
print(is_pangramma_ascii(input.lower()))