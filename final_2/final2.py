import argparse
import final_2.DB as DB
import final_2.rest as krug
import urllib3
import codecs


DB.CreateDB().create_db()
DB.CreateTables().create_tables()

skill = DB.InsSkills()


parser = krug.MyHTMLParser()


reader = codecs.getreader('utf-8')
urllib3.disable_warnings()
http = urllib3.PoolManager()
response = http.request('GET', 'https://moikrug.ru/vacancies', preload_content=False)
if response.status != 200:
    print("Don't find pokemon.")
    exit(0)
parser.feed(response.data.decode('utf-8'))

#print(parser.insert.insert)
skill.insert(parser.insert.insert)