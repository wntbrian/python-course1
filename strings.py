###
### Задание 1, Вариант 2, Строки №6
###
#Функция подсчета уникальных букв в строке
def is_pangramma(str):
    if len(str) == 0: #Если строка в рекурсии закончилась, выходим из рекурсии
        return 0
    else:
        if str[0] in str[1:]: #Проверяем содержится ли первая буква в строке, в оставшейся части строки
            return 0 + is_pangramma(str[1:]) #Cодержится, возвращаем ноль, отдаем на проверку оставшиеся буквы
        else:
            return 1 + is_pangramma(str[1:]) #Буква не содержится, вовращаем 1 и передаем остаток

#Функция поиска букв в строке, из плюсов не требует ничего делать с пробелами и лишними символами
def is_pangramma_ascii(str):
    if len(str) >= 26:
        for i in range(26):
            if chr(ord('a') + i) not in str:
                return str+" \nне является панграммой"
            else:
                if i == 25:
                    return str+" \n является панграммой"
        return str + " \nне является панграммой"
    else:
        return "не хватает букв"

#
## Подготовка данных
#
#вводимая строка
#input="asdfghjklasdfghjklasdfghjklasdfghjklqwertyuioppoiuytrewqzxcvbnmZXCVBNMJYTREWSXCVGHYUI"

#ручной ввод
input=input("Введите строку для проверки: ")

def prepare_string(string):
#string='' # Объявляка (без нее не захотела, надо разобраться.
# Сплитм строку по пробелам, потом клеим в строку
    for part in input.split( ):
        string += part
    if is_pangramma(string.lower()) == 26:
        return "  Введенная строка:\n   "+string+"\n   является панграммой."
    else:
        return "  Введенная строка:\n   " + string + "\n   не является панграммой, т.к. не уникальных хватает букв, а больше 26 их быть не может по условию"

print (" Вариант Рекурсия (работает исключительно критериям задачи на вводную строку:")
print (prepare_string(input))

print (" Вариант ASCII:")
print(is_pangramma_ascii(input.lower()))