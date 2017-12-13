import re

class ReadTag():
    TAGS = []
    CLASS = []
    value = int()
    skills = []
    titles = []
    result = []
    def __init__(self):
        print('init')
    def reciver(self,position='',tag='',attr='',data=''):
        if tag:
            if position == 'start':
                self.TAGS.append(tag)
            if self.TAGS and position == 'stop' and self.TAGS[-1] == tag:
                del self.TAGS[-1]
                # if self.TAGS[] == 0:
                #     self.CLASS = []
        if attr:
            if self.TAGS:
                if attr[0] == 'class':
                    if attr[1] == 'info':
                        try:
                            d = {"skills":self.skills, "vacancy_url":self.url, "title":self.name, "company":self.company, "company_url":self.company_url}
                            self.result.append(d)
                        except:
                            print ("first run")
                        self.CLASS = []
                        self.skills = []
                    self.CLASS.append(attr[1])
                if self.CLASS:
                # if attr[0] == 'class' and attr[1] == 'info' and self.TAGS[-1] == 'div':
                #     self.CLASS.append(attr[1])
                                    # if attr[0] == 'class' and attr[1] == 'skills' and self.CLASS[-1] == 'title':
                    #     self.CLASS.append(attr[1])
                    # if attr[0] == 'class' and attr[1] == 'title' and self.CLASS[-1] == 'info':
                    #     self.CLASS.append(attr[1])
                    # if attr[0] == 'class' and attr[1] == 'company_name' and self.CLASS[-1] == 'skill':
                    #     self.CLASS.append(attr[1])
                    if attr[0] == 'title' and self.CLASS[-1] == 'title':
                        self.name = attr[1]
                    if self.TAGS[-1] == 'a':
                        # if self.CLASS[-1] == 'skills' and attr[1] == 'skill':
                        #     self.CLASS.append(attr[1])
                        if attr[0] == 'href' and self.CLASS[-1] == 'title':
                            self.url = attr[1]
                        if attr[0] == 'href' and self.CLASS[-1] == 'company_name':
                            self.company_url = attr[1]
                        if attr[0] == 'href' and self.CLASS[-1] == 'skill':
                            self.value = re.split('[^0-9.]+', attr[1])[-1]
        if data:
            if self.CLASS:
                if self.TAGS[-1] == 'a':
                    # if self.CLASS[-1] == 'title':
                    #     self.name = data
                    if self.CLASS[-1] == 'skill':
                        self.skills.append([self.value] + [data])
                    if self.CLASS[-1] == 'company_name':
                        self.company = data
                if self.CLASS[-1] == "salary":
                    self.salary = data

