from urllib import request
from html.parser import HTMLParser
from html.entities import name2codepoint
import urllib3
import codecs
from final_2.inputer import ReadTag

class MyHTMLParser(HTMLParser):
    insert = ReadTag()
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        self.insert.reciver(position='start',tag=tag)
        for attr in attrs:
            print("     attr:", attr)
            self.insert.reciver(attr=attr)

    def handle_endtag(self, tag):
        print("End tag  :", tag)
        self.insert.reciver(position='stop',tag=tag)

    def handle_data(self, data):
        print("Data     :", data)
        self.insert.reciver(data=data)

    # def handle_comment(self, data):
    #     print("Comment  :", data)
    #
    # def handle_entityref(self, name):
    #     c = chr(name2codepoint[name])
    #     print("Named ent:", c)
    #
    # def handle_charref(self, name):
    #     if name.startswith('x'):
    #         c = chr(int(name[1:], 16))
    #     else:
    #         c = chr(int(name))
    #     print("Num ent  :", c)
    #
    # def handle_decl(self, data):
    #     print("Decl     :", data)

