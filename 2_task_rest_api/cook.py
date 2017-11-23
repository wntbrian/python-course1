"""
Проверим ваш творческий потенциал. В общем, задача простая: с помощью библиотеки urllib получить данные с разных API сервисов и предоставить в человекочитаемом виде.
Ссылочка на библиотеку тут: https://docs.python.org/3/library/urllib.html
Для каждого API есть ряд своих условий:
Список API:

http://www.recipepuppy.com/about/api/ - это сервис для получения рецептов. Задача простая: передаем список продуктов,
получаем рецепты для этого списка продуктов
"""


from urllib import request, error
from json import load
import webbrowser


def recipepuppy(url='http://www.recipepuppy.com/api/', lts=['onions','garlic'], p=1, err=0):
    str_url = url+'?i='+','.join(lts)+'&p={}'.format(p)

    try:
        response = request.urlopen(str_url)
    except error.HTTPError:
        if err > 3:
            print("End of recipe list")
            return 0
        recipepuppy(url, lts, p + 1, err+1)

    data = load(response)
    for num, select in enumerate(data['results']):
        print("{} - {}".format(num,select['title'].strip()))
    choose = input("Input your choose:")
    if choose == 'n':
        recipepuppy(url,lts,p+1)
    try:
        int_ch = int(choose)
        webbrowser.open(data['results'][int_ch]['href'])
    except ValueError:
        print("Incorrect type")
        recipepuppy(url, lts, p, err)

ingre = input("Enter list of ingredients separate by space: ").split()
recipepuppy('http://www.recipepuppy.com/api/',ingre)