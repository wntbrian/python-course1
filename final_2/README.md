# Финальное задание №2

## Задание
### HTML Parse
https://moikrug.ru
-
Необходимо получить html-документ и его распарсить. Стягиваем данные по заголовкам статей, пользователей и хэш-тэгам.
###  Выборки
 1. Получим список вакансий по заданному хэш-тэгу(скилу) в заданном интервале запрлаты;
 2. Получаем список высокоплачиваемых вакансей по заданному скилу;
 3. Получаем топ 10 популярных скилов, т.е. те, у которых больше всего вакансий;
 4. Получаем список самых активных компаний, те, у которых больше всего вакансий.
 
### Доп. условия
- Параметры для запроса задаются в командной строке как аргументы для интерпретатора. Для этого юзаем библиотеку argparse. 
- Для связки с базой используем модуль psycorpg2. 
- Для парсинга - html.parse. 
- Для работы с запросами - urllib.

## Реализация
### Установка
```apt-get install python3```

```pip instal urllib3 psycopg2 terminaltables```
### Файл конфигурации для подключения к БД
postgres.ini
```ini
[DATABASE]
PG_HOST = localhost
PG_DB = final
PG_USER = postgres
PG_PASS = password
```
### Схема БД
```sql
CREATE TABLE skill (
        id integer PRIMARY KEY,
        description varchar(255)
        ) 
CREATE TABLE skill_map (
                    vacancy integer references vacancy(id),
                    skill integer references skill(id)
                    ) 
CREATE TABLE vacancy (
                    id SERIAL PRIMARY KEY,
                    company integer references company(id),
                    title varchar(255),
                    url varchar(255),
                    salary_start integer,
                    salary_end integer
                    ) 
CREATE TABLE company (
                      id SERIAL PRIMARY KEY,
                      name varchar(255),
                      url varchar(255)
                      ) 
```
### Примеры использования
Инициализация БД и загрузка данных с moikrug.ru
```commandline
python index.py -load
```
Поиск вакансий по вашим умениям
```commandline
python index.py -skill python postgresql
```
Самый популятрые навыки(скилы)
```commandline
python index.py -top
```
Самый активные компании
```commandline
python index.py -company
```