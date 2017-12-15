from html.parser import HTMLParser
from MoiKrugParser import TagParser


class MyHTMLParser(HTMLParser):

    content = TagParser()

    def handle_starttag(self, tag, attrs):
        #print("Start tag:", tag)
        self.content.load(position='start',tag=tag)
        for attr in attrs:
            #print("     attr:", attr)
            self.content.load(attr=attr)

    def handle_endtag(self, tag):
        #print("End tag  :", tag)
        self.content.load(position='stop',tag=tag)

    def handle_data(self, data):
        #print("Data     :", data)
        self.content.load(data=data)