import re

class ReadTag():
    TAGS = []
    CLASS = []
    value = int()
    insert = []
    def __init__(self):
        print('init')
    def reciver(self,position='',tag='',attr='',data=''):
        if tag:
            if position == 'start':
                self.TAGS.append(tag)
            if self.TAGS and position == 'stop' and self.TAGS[-1] == tag:
                if tag == 'a' and self.CLASS and self.CLASS[-1] == 'skill':
                    self.CLASS = []
                del self.TAGS[-1]
                # if self.TAGS[] == 0:
                #     self.CLASS = []
        if attr:
            if self.TAGS:
                if attr[0] == 'class' and attr[1] == 'skills' and self.TAGS[-1] == 'div':
                    self.CLASS.append(attr[1])
                if self.CLASS:
                    if self.TAGS[-1] == 'a':
                        if self.CLASS[-1] == 'skills' and attr[1] == 'skill':
                            self.CLASS.append(attr[1])
                        if self.CLASS[-1] == 'skill' and attr[0] == 'href':
                            self.value = re.split('[^0-9.]+', attr[1])[-1]
        if data:
            if self.CLASS:
                if self.TAGS[-1] == 'a' and self.CLASS[-1] == 'skill':
                    self.insert.append(tuple([self.value] + [data]))
