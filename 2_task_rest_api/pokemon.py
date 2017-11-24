"""
Проверим ваш творческий потенциал. В общем, задача простая: с помощью библиотеки urllib получить данные с разных API сервисов и предоставить в человекочитаемом виде.
Ссылочка на библиотеку тут: https://docs.python.org/3/library/urllib.html
Для каждого API есть ряд своих условий:
Список API:

https://pokeapi.co/ - ПОКЕМОНЫ!!! Тут собрана вся информация о покемонах. Необходимо получить номер покемона и выдать
краткую информацию о нем.
"""


from json import load
import urllib3
import codecs
from sys import exit


def pokemon(url='https://pokeapi.co/api/v2/pokemon/', idx='1'):
    reader = codecs.getreader('utf-8')
    urllib3.disable_warnings()
    http = urllib3.PoolManager()
    response = http.request('GET', url+idx, preload_content=False)
    if response.status != 200:
        print("Don't find pokemon with ID: {}, Sorry".format(idx))
        exit(0)
    data = load(reader(response))
    response.release_conn()
    stats_name = {}
    for num, stat in enumerate(data['stats']):
        stats_name[stat['stat']['name']] = num
    print('Pokemon: {}                '.format(data['name']))
    print('Stats:                ')
    print('                 HP               ')
    print('                 {}               '.format(data['stats'][stats_name['hp']]['base_stat']))
    print('                 __              ')
    print('               /    \             ')
    print('     Sp.Atk  /        \    Attack ')
    print('       {}  /            \   {}  '.format(data['stats'][stats_name['special-attack']]['base_stat'],data['stats'][stats_name['attack']]['base_stat']))
    print('         |                |     ')
    print('         |                |       ')
    print('         |                |       ')
    print('         |                |     ')
    print('      {}   \            /  {} '.format(data['stats'][stats_name['special-defense']]['base_stat'],data['stats'][stats_name['defense']]['base_stat']))
    print('     Sp. Def \        /    Defense')
    print('               \ __ /      ')
    print('                 {}         '.format(data['stats'][stats_name['speed']]['base_stat']))
    print('                Speed         ')

choose = input("Input your pokemon ID:")
pokemon('https://pokeapi.co/api/v2/pokemon/', choose)