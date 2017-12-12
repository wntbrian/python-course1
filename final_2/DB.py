import psycopg2

PG_HOST = "192.168.0.149"
PG_DB = "final_2"
PG_USER = "postgres"
PG_PASS = "password"


class CreateDB:
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
    @staticmethod
    def create_tables():
        """ create tables in the PostgreSQL database"""
        commands = (
            """CREATE TABLE skills (
                    id integer PRIMARY KEY,
                    description varchar(255)
                    ) 
            """,)
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
        """ insert multiple products into the products table  """
        def __init__(self):
            self.sql = ""
        self.conn = None
        try:
            self.conn = psycopg2.connect(host=PG_HOST, database=PG_DB, user=PG_USER, password=PG_PASS)
            self.cur = self.conn.cursor()
            self.cur.executemany(self.sql, data)
            self.conn.commit()
            self.cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()


class InsSkills(InsertIntoTables):
    def __init__(self):
        self.sql = "INSERT INTO skills VALUES(%s,%s);"