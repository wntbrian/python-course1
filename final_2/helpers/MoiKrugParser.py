import re


class TagParser:

    def __init__(self):
        self.dryrun()

    def dryrun(self):
        self.TAGS = []
        self.CLASS = []
        self.skills = []
        self.result = []
        self.value = int()
        self.salary = ""
        self.company = ""

    def load(self,position='',tag='',attr='',data=''):
        LASTITEM = -1
        if tag:
            if position == 'start':
                self.TAGS.append(tag)
            if self.TAGS and position == 'stop' and self.TAGS[-1] == tag:
                del self.TAGS[-1]
        if attr:
            if self.TAGS:
                if attr[0] == 'class':
                    if attr[1] == 'info':
                        if self.salary:
                            self.salary_start = re.findall('[оО]т\s[0-9]+\s[0-9]+', self.salary)
                            self.salary_end = re.findall('[дД]о\s[0-9]+\s[0-9]+', self.salary)
                            if self.salary_start:
                                self.salary_start = re.sub(r'[\D]', '', self.salary_start[0])
                            else:
                                self.salary_start = None
                            if self.salary_end:
                                self.salary_end = re.sub(r'[\D]', '', self.salary_end[0])
                            else:
                                self.salary_end = None
                        else:
                            self.salary_start = None
                            self.salary_end = None
                        if self.company:
                            try:
                                d = {"skills": self.skills, "vacancy_url": self.url, "title": self.name,
                                     "company": self.company, "company_url": self.company_url,
                                     "salary_start": self.salary_start, "salary_end": self.salary_end}
                                self.result.append(d)
                            except:
                                print ("Skipped")
                        self.CLASS = []
                        self.skills = []
                        self.salary = ""
                    self.CLASS.append(attr[1])
                if self.CLASS:
                    if attr[0] == 'title' and self.CLASS[-1] == 'title':
                        self.name = attr[1]
                    if self.TAGS[LASTITEM] == 'a':
                        if attr[0] == 'href' and self.CLASS[LASTITEM] == 'title':
                            self.url = attr[1]
                        if attr[0] == 'href' and self.CLASS[LASTITEM] == 'company_name':
                            self.company_url = attr[1]
                        if attr[0] == 'href' and self.CLASS[LASTITEM] == 'skill':
                            self.value = re.split('[^0-9.]+', attr[1])[LASTITEM]
        if data:
            if self.CLASS:
                if self.TAGS[LASTITEM] == 'a':
                    if self.CLASS[LASTITEM] == 'skill':
                        self.skills.append([self.value] + [data])
                    if self.CLASS[LASTITEM] == 'company_name':
                        self.company = data
                if self.CLASS[LASTITEM] == "count" and self.CLASS[-2] == "salary":
                    self.salary += data