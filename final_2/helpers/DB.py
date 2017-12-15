import psycopg2
import configparser


config = configparser.ConfigParser()
config.read('postgres.ini')
PG_HOST = config['DATABASE']['PG_HOST']
PG_DB = config['DATABASE']['PG_DB']
PG_USER = config['DATABASE']['PG_USER']
PG_PASS = config['DATABASE']['PG_PASS']


class CreateDB:
    """
    Создание БД в чистом сервере.
    """
    @staticmethod
    def create_db():
        try:
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(host=PG_HOST, database="postgres", user=PG_USER, password=PG_PASS)
            conn.set_session(autocommit=True)
            cur = conn.cursor()
            print('PostgreSQL database create: {} '.format(PG_DB))
            cur.execute('CREATE DATABASE {};'.format(PG_DB))
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')


class CreateTables:
    """
    Создание схемы в БД.
    """
    @staticmethod
    def create_tables():
        """ create tables in the PostgreSQL database"""
        commands = (
            """CREATE TABLE skill (
                    id integer PRIMARY KEY,
                    description varchar(255)
                    ) 
            """,
            """CREATE TABLE company (
                                  id SERIAL PRIMARY KEY,
                                  name varchar(255),
                                  url varchar(255)
                                  ) 
                                  """,
            """CREATE TABLE vacancy (
                                id SERIAL PRIMARY KEY,
                                company integer references company(id),
                                title varchar(255),
                                url varchar(255),
                                salary_start integer,
                                salary_end integer
                                ) 
                                """,
            """CREATE TABLE skill_map (
                                vacancy integer references vacancy(id),
                                skill integer references skill(id)
                                ) 
                        """
        )
        conn = None
        try:
            conn = psycopg2.connect(host=PG_HOST, database=PG_DB, user=PG_USER, password=PG_PASS)
            cur = conn.cursor()
            for command in commands:
                cur.execute(command)
            cur.close()
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


class InsertIntoTables:
    def insert(self,data):
        """ insert multiple into tables  """
        def __init__(self):
            self.sql = ""
        self.conn = None
        self.conn = psycopg2.connect(host=PG_HOST, database=PG_DB, user=PG_USER, password=PG_PASS)
        self.cur = self.conn.cursor()
        for s in data:
            try:
                self.cur.execute(self.sql, s)
            except (Exception, psycopg2.DatabaseError) as error:
                self.error = error
            finally:
                self.conn.commit()
        if self.conn is not None:
            self.conn.close()


class Select:
    @staticmethod
    def select(sql):
        """ query select from the table """
        conn = None
        rows = ""
        try:
            conn = psycopg2.connect(host=PG_HOST, database=PG_DB, user=PG_USER, password=PG_PASS)
            cur = conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
            return rows


class InsSkills(InsertIntoTables):
    def __init__(self):
        self.sql = "INSERT INTO skill VALUES(%s,%s);"

class InsSkillMap(InsertIntoTables):
    def __init__(self):
        self.sql = "INSERT INTO skill_map VALUES(%s,%s);"

class InsVacancy(InsertIntoTables):
    def __init__(self):
        self.sql = "INSERT INTO vacancy (company, title, url, salary_start, salary_end) VALUES (%s,%s,%s,%s,%s);"

class InsCompany(InsertIntoTables):
    def __init__(self):
        self.sql = "INSERT INTO company (name, url) VALUES(%s,%s);"