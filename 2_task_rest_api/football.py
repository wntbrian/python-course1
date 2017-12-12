"""
Проверим ваш творческий потенциал. В общем, задача простая: с помощью библиотеки urllib получить данные с разных API сервисов и предоставить в человекочитаемом виде.
Ссылочка на библиотеку тут: https://docs.python.org/3/library/urllib.html
Для каждого API есть ряд своих условий:
Список API:

https://api.football-data.org/ - это сервис о футболе. Задача несложная предоставить информацию о ТОП-5 популярных
чемпионатах. Вывести по каждому чемпионату первые пять команд с наибольшим числом забитых голов.
"""


from urllib import request, error
from json import load
from sys import exit


def football(url='http://api.football-data.org/v1/competitions/?season=', season='2016', sort_dict='numberOfGames'):
    try:
        response = request.urlopen(url+season)
    except error.HTTPError:
        print('Incorrect input')
        exit(0)
    data = load(response)
    data.sort(key=lambda x: x[sort_dict],reverse=True) ### Считаю, что популяроность - кол-во игр.
    for leag_num, comp in enumerate(data):
        if leag_num >= 4:
            break
        try:
            leagueTable = load(request.urlopen(comp['_links']['leagueTable']['href']))
        except error.HTTPError as err:
            if err.code == 403:
                print("History data deny for public access")
                continue
        leagueTable['standing'].sort(key=lambda x: x['goalsAgainst'], reverse=True)
        print(leagueTable['leagueCaption'])
        for num, stats in enumerate(leagueTable['standing']):
            print(" - {}".format(stats['teamName']))
            if num >= 4:
                break

choose = input("Enter year of sesson for search:")
football('http://api.football-data.org/v1/competitions/?season=', choose)