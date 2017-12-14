import argparse
import final_2.DB as DB
import final_2.htmlparse as moikrug
import urllib3
import codecs


# Table init
DB.CreateDB().create_db()
DB.CreateTables().create_tables()

# Inserts init
skill = DB.InsSkills()
company = DB.InsCompany()
vacancy = DB.InsVacancy()
skill_map = DB.InsSkillMap()
select = DB.Select()

data = moikrug.MyHTMLParser()
reader = codecs.getreader('utf-8')
urllib3.disable_warnings()
http = urllib3.PoolManager()


def LoadDB():
    page, page_end, error = 1, 0
    vacancyBank = []
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
        vacancyBank.append(data.content.result)
        print(page)
        page = page + 1
        data.content.dryrun()
    for vac in vacancyBank:
        for items in vac:
            skill.insert(items['skills'])
            company_id = select.select("SELECT id FROM company WHERE name = '{}'".format(items['company']))
            if not company_id:
                company.insert([[items['company'], items['company_url']]])
                company_id = select.select("SELECT id FROM company WHERE name = '{}'".format(items['company']))
            vacancy_id = select.select("SELECT id FROM vacancy WHERE url = '{}'".format(items['vacancy_url']))
            if not vacancy_id:
                vacancy.insert([[company_id[0][0], items['title'], items['vacancy_url'], items['salary_start'], items['salary_end']]])
                vacancy_id = select.select("SELECT id FROM vacancy WHERE url = '{}'".format(items['vacancy_url']))
                for vac_skill in items['skills']:
                    skill_map.insert([[vacancy_id[0][0], vac_skill[0]]])

