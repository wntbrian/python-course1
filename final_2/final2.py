import argparse
import final_2.DB as DB
import final_2.rest as krug
import urllib3
import codecs


DB.CreateDB().create_db()
DB.CreateTables().create_tables()

skill = DB.InsSkills()
company = DB.InsCompany()
vacancy = DB.InsVacancy()
skill_map = DB.InsSkillMap()

parser = krug.MyHTMLParser()


reader = codecs.getreader('utf-8')
urllib3.disable_warnings()
http = urllib3.PoolManager()
response = http.request('GET', 'https://moikrug.ru/vacancies', preload_content=False)
if response.status != 200:
    print("Don't find pokemon.")
    exit(0)
parser.feed(response.data.decode('utf-8'))

sel = DB.Select()
#print(parser.insert.insert)
sk = parser.insert.result
for t in sk:
    skill.insert(t['skills'])
    company_id = sel.select("SELECT id FROM company WHERE name = '{}'".format(t['company']))
    if not company_id:
        company.insert([[t['company'], t['company_url']]])
        company_id = sel.select("SELECT id FROM company WHERE name = '{}'".format(t['company']))
    vacancy_id = sel.select("SELECT id FROM vacancy WHERE url = '{}'".format(t['vacancy_url']))
    if not vacancy_id:
        vacancy.insert([[company_id[0][0], t['title'], t['vacancy_url']]])
        vacancy_id = sel.select("SELECT id FROM vacancy WHERE url = '{}'".format(t['vacancy_url']))
        for vac_skill in t['skills']:
            skill_map.insert([[vacancy_id[0][0], vac_skill[0]]])
    print("")