# -*- coding: utf-8 -*-


import argparse
import helpers.final2 as final2
from terminaltables import AsciiTable

final = final2.Final2()
parser = argparse.ArgumentParser()
parser.add_argument("-min", type=int, nargs="?",
                    help="Минимальный уровень вашей ЗП")
parser.add_argument("-max", type=int, nargs="?",
                    help="Максимальный уровень вашей ЗП")
parser.add_argument("-skills", "-s", nargs="+",
                    help="Ваши скилы")
parser.add_argument("-top", "-t", action="store_true",
                    help="Топ скилов")
parser.add_argument("-company", "-c", action="store_true",
                    help="Топ компаний по кол-ву вакансий")
parser.add_argument("-load", "-l", action="store_true",
                    help="Создание и Загрузка БД с moikrug.ru")
parser.add_argument("-page", "-p", type=int, nargs="?",
                    help="Ограничение в страницах")
args = parser.parse_args()


if args.load:
    if args.page:
        final.load_db(args.page)
    else:
        final.load_db()

if (args.min or args.max) and args.skills:
    NAME = 0
    COMPANY = 1
    URL = 2
    MIN = 3
    MAX = 4
    result = final.select_skill_salary(args.min,args.max,args.skills)
    if result:
        table_data = [['Вакансия', 'Комания','Ссылка','Минимальная ЗП','Максимальная ЗП']]
        for line in result:
            table_data.append([line[NAME], line[COMPANY], "https://moikrug.ru"+line[URL], line[MIN], line[MAX]])
        table = AsciiTable(table_data, "Вакансии по навыкам c учетом ЗП: {}".format(", ".join(args.skills)))
        print(table.table)

if args.skills:
    NAME = 0
    COMPANY = 1
    URL = 2
    MIN = 3
    MAX = 4
    result = final.select_company_by_skill(args.skills)
    if result:
        table_data = [['Вакансия', 'Комания','Ссылка','Минимальная ЗП','Максимальная ЗП']]
        for line in result:
            table_data.append([line[NAME], line[COMPANY], "https://moikrug.ru"+line[URL], line[MIN], line[MAX]])
        table = AsciiTable(table_data, "Самый высокооплачиваемые вакансии по навыкам: {}".format(", ".join(args.skills)))
        print(table.table)

if args.top:
    NAME = 1
    COUNT = 2
    result = final.select_top_skills()
    if result:
        table_data = [['Навык', 'Кол-во']]
        for line in result:
            table_data.append([line[NAME], line[COUNT]])
        table = AsciiTable(table_data, "ТОП 10 часто вречающихся навыков")
        print(table.table)

if args.company:
    NAME = 1
    AVG = 3
    V_COUNT = 4
    MIN = 5
    MAX = 6
    result = final.select_top_company()
    if result:
        table_data = [['Компания', 'Средняя ЗП','Кол-во вакансий','Минимальная ЗП','Максимальная ЗП']]
        for line in result:
            table_data.append([line[NAME], line[AVG], line[V_COUNT], line[MIN], line[MAX]])
        table = AsciiTable(table_data, "Самые богатые компании")
        print(table.table)