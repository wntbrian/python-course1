"""
Проверим ваш творческий потенциал. В общем, задача простая: с помощью библиотеки urllib получить данные с разных API сервисов и предоставить в человекочитаемом виде.
Ссылочка на библиотеку тут: https://docs.python.org/3/library/urllib.html
Для каждого API есть ряд своих условий:
Список API:

http://open-notify.org/Open-Notify-API/ISS-Location-Now/ - это сервис, которые предоставляет информацию о геолокации
Международной Космической станции. Ваша задача за показать в какой точке мира находится станция сейчас.
"""


from urllib import request
from json import load
import webbrowser


def ISS(url='http://api.open-notify.org/iss-now.json'):
    response = request.urlopen(url)
    data = load(response)
    print("Opening browser...")
    webbrowser.open('https://www.openstreetmap.org/?mlat={0}&mlon={1}#map=4/{0}/{1}'.format(data['iss_position']['latitude']
,data['iss_position']['longitude']))
    #ISS(url) ### Бессмертный? Раскомментируй ;)

ISS()