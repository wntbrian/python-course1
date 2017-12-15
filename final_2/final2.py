import DB as DB
import htmlparse as moikrug
import urllib3


class Final2:
    def __init__(self):
        self.skill = DB.InsSkills()
        self.company = DB.InsCompany()
        self.vacancy = DB.InsVacancy()
        self.skill_map = DB.InsSkillMap()
        self.select = DB.Select()

    def load_db(self,page_end=100):
        # Table init
        DB.CreateDB().create_db()
        DB.CreateTables().create_tables()

        data = moikrug.MyHTMLParser()
        urllib3.disable_warnings()
        http = urllib3.PoolManager()
        page, error = 1, 0
        vacancybank = []

        print("Загрузка Данных")
        while page > 0:
            response = http.request('GET', 'https://moikrug.ru/vacancies?page={}'.format(page), preload_content=False)
            if response.status != 200:
                print("Don't find internet or site is down.")
                error = error + 1
                if error > 5:
                    break
            if page > page_end:
                break
            data.feed(response.data.decode('utf-8'))
            if len(data.content.result) < 6:
                break
            vacancybank.append(data.content.result)
            print('.', sep=' ', end='', flush=True)
            page = page + 1
            data.content.dryrun()
        print ("Всего получено {} страниц".format(page-1))

        print ("\nЗагрузка БД")
        for vac in vacancybank:
            for items in vac:
                print('.', sep=' ', end='', flush=True)
                self.skill.insert(items['skills'])
                company_id = self.select.select("SELECT id FROM company WHERE name = '{}'".format(items['company']))
                if not company_id:
                    self.company.insert([[items['company'], items['company_url']]])
                    company_id = self.select.select("SELECT id FROM company WHERE name = '{}'".format(items['company']))
                vacancy_id = self.select.select("SELECT id FROM vacancy WHERE url = '{}'".format(items['vacancy_url']))
                if not vacancy_id:
                    self.vacancy.insert([[company_id[0][0], items['title'], items['vacancy_url'], items['salary_start'],
                                     items['salary_end']]])
                    vacancy_id = self.select.select("SELECT id FROM vacancy WHERE url = '{}'".format(items['vacancy_url']))
                    for vac_skill in items['skills']:
                        self.skill_map.insert([[vacancy_id[0][0], vac_skill[0]]])

    def select_skill_salary(self,min='',max='',skills=[]):
        sql = """select v.title, c.name, v.url, v.salary_start, v.salary_end
        from vacancy v, company c
        where	v.company = c.id"""
        if max:
            sql += " and (v.salary_start <= {0} or v.salary_start is null or {0} is null)".format(max)
        if min:
            sql += " and (v.salary_end >= {0} or v.salary_end is null or {0} is null)".format(min)
        if skills:
            sql += " and {} = ( select count(1) ".format(len(skills))
            sql += """ from skill_map inner join skill on skill.id = skill_map.skill
                   where v.id = skill_map.vacancy
                   and lower(skill.description) in ("""
            for skill in skills:
                sql += "'"+skill.lower()+"',"
            sql = sql[:-1]
            sql += "))"
        sql += " order by v.salary_start desc nulls last, v.salary_end"
        result = self.select.select(sql)
        return result

    def select_company_by_skill(self,skill):
        sql = """select v.title, c.name, v.url, v.salary_start, v.salary_end
        from vacancy v, company c, skill_map sm, skill s
        where	v.company = c.id
        and sm.vacancy = v.id
        and sm.skill = s.id"""
        sql += " and lower(s.description) = '{}'".format(skill[0].lower())
        sql += " order by v.salary_start desc NULLS last, v.salary_end desc NULLS last"
        result = self.select.select(sql)
        return result

    def select_top_skills(self):
        sql = """select *
        from (
        select t.id, t.descr, t.cnt, 
        dense_rank() over (order by t.cnt desc) r
        from (
        select s.id id, s.description descr, count(1) cnt
        from vacancy v, skill_map sm, skill s
        where	sm.vacancy = v.id
        and sm.skill = s.id
        group by s.id, s.description
        ) t
        ) t2
        where t2.r <= 10
            """
        result = self.select.select(sql)
        return result

    def select_top_company(self):
        sql = """select c.id, c.name, sum(v.salary_start), round(avg(v.salary_start)), count(1), min(v.salary_start), max(v.salary_start)
        from vacancy v, company c
        where	v.company = c.id and v.salary_start is not null
        group by c.id, c.name
        order by sum(v.salary_start) desc
        """
        result = self.select.select(sql)
        return result