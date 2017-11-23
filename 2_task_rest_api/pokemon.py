"""
Проверим ваш творческий потенциал. В общем, задача простая: с помощью библиотеки urllib получить данные с разных API сервисов и предоставить в человекочитаемом виде.
Ссылочка на библиотеку тут: https://docs.python.org/3/library/urllib.html
Для каждого API есть ряд своих условий:
Список API:

https://pokeapi.co/ - ПОКЕМОНЫ!!! Тут собрана вся информация о покемонах. Необходимо получить номер покемона и выдать
краткую информацию о нем.
"""


from urllib import request, error
from json import load
import webbrowser

def pokemon(url='https://pokeapi.co/api/v2/pokemon/1/'):
    response = request.urlopen(url)
    data = load(response)
    print(data)

pokemon()