from html.parser import HTMLParser
from helpers.MoiKrugParser import TagParser


class MyHTMLParser(HTMLParser):
    """
    Обработчик вызова функция для парсинга страницы
    """
    content = TagParser()

    def handle_starttag(self, tag, attrs):
        self.content.load(position='start',tag=tag)
        for attr in attrs:
            self.content.load(attr=attr)

    def handle_endtag(self, tag):
        self.content.load(position='stop',tag=tag)

    def handle_data(self, data):
        self.content.load(data=data)