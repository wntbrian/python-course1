###
### Задание 1, Вариант 2, Строки №6
###

#Функция подсчета уникальных букв в строке
def isPangramma(str):
    if len(str) == 0: #Если строка в рекурсии закончилась, выходим из рекурсии
        return 0
    else:
        if str[0] in str[1:]: #Проверяем содержится ли первая буква в строке, в оставшейся части строки
            return 0 + isPangramma(str[1:]) #Cодержится, возвращаем ноль, отдаем на проверку оставшиеся буквы
        else:
            return 1 + isPangramma(str[1:]) #Буква не содержится, вовращаем 1 и передаем остаток
#Функция поиска букв в строке
def isPangramma_ascii(str):
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
input="qwertyuiopasdfghjklzxcvbnzzs"  #вводимая строка
string='' # Объявляка (без нее не захотела, надо разобраться.
# Сплитм строку по пробелам, потом клеим в строку
for part in input.split( ):
    string += part
print (" Вариант Рекурсия:")
if isPangramma(string.lower()) == 26:
    print ("  Введенная строка:\n   "+string+"\n   является панграммой.")
else:
    print("  Введенная строка:\n   " + string + "\n   не является панграммой, т.к. не уникальных хватает букв, а больше 26 их быть не может по условию")
print (" Вариант ASCII:")
print(isPangramma_ascii(string.lower()))