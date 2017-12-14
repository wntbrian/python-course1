import argparse
import final_2.final2 as final2

final = final2.Final2()
parser = argparse.ArgumentParser()
parser.add_argument("-DB", "-d", type=str, nargs="?",
                    help="Адрес БД (localhost)")
parser.add_argument("-User", "-u", type=str, nargs="?",
                    help="Пользователь БД")
parser.add_argument("-Pass", "-p", type=str, nargs="?",
                    help="Пароль БД")
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
args = parser.parse_args()

#if (args['DB']):
#    final2.Final2.load_db()

print(final.select_skill_salary(args.min,args.max,args.skills))
print()
print(final.select_company_by_skill(args.skills))
print()
print(final.select_top_skills())
print()
print(final.select_top_company())
print()
print(args)