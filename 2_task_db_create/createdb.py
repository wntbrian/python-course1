import psycopg2

HOST = "postgres_server"
DB = "task_py"
PG_USER = "postgres"
PG_PASS = "password"


def create_db():
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host=HOST, database="postgres", user=PG_USER, password=PG_PASS)
        conn.set_session(autocommit=True)
        cur = conn.cursor()
        print('PostgreSQL database create: {} '.format(DB))
        cur.execute('CREATE DATABASE {};'.format(DB))
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """ CREATE TABLE Product (
                maker varchar(255),
                model varchar(255) UNIQUE,
                "type" varchar(255)
                ) 
        """,
        """ CREATE TABLE PC (
                code integer PRIMARY KEY,
                model varchar(255) references Product(model),
                speed integer,
                ram integer,
                hd integer,
                cd varchar(4),
                price integer
                )
        """,
        """ CREATE TABLE Laptop (
                code integer PRIMARY KEY,
                model varchar(255) references Product(model),
                speed integer,
                ram integer,
                hd integer,
                screen integer,
                price integer
                )
        """,
        """ CREATE TABLE Printer (
                code integer PRIMARY KEY,
                model varchar(255) references Product(model),
                color varchar(1),
                "type" varchar(6),
                price integer
                )
        """)
    conn = None
    try:
        conn = psycopg2.connect(host=HOST, database=DB, user=PG_USER, password=PG_PASS)
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


def insert_product(products):
    """ insert multiple products into the products table  """
    sql = "INSERT INTO Product VALUES(%s,%s,%s);"
    conn = None
    try:
        conn = psycopg2.connect(host=HOST, database=DB, user=PG_USER, password=PG_PASS)
        cur = conn.cursor()
        cur.executemany(sql,products)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_pc(pc):
    """ insert multiple pc into the pc table  """
    sql = "INSERT INTO PC VALUES(%s,%s,%s,%s,%s,%s,%s);"
    conn = None
    try:
        conn = psycopg2.connect(host=HOST, database=DB, user=PG_USER, password=PG_PASS)
        cur = conn.cursor()
        cur.executemany(sql, pc)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_laptop(laptop):
    """ insert multiple laptop into the laptop table  """
    sql = "INSERT INTO Laptop VALUES(%s,%s,%s,%s,%s,%s,%s);"
    conn = None
    try:
        conn = psycopg2.connect(host=HOST, database=DB, user=PG_USER, password=PG_PASS)
        cur = conn.cursor()
        cur.executemany(sql, laptop)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_printer(printer):
    """ insert multiple printer into the printer table  """
    sql = "INSERT INTO Printer VALUES(%s,%s,%s,%s,%s);"
    conn = None
    try:
        conn = psycopg2.connect(host=HOST, database=DB, user=PG_USER, password=PG_PASS)
        cur = conn.cursor()
        cur.executemany(sql, printer)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def select(sql):
    """ query select from the table """
    conn = None
    try:
        conn = psycopg2.connect(host=HOST, database=DB, user=PG_USER, password=PG_PASS)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        print("\n{} :".format(sql))
        for row in rows:
            print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


create_db()

create_tables()

insert_product([
    ('Asus', 'T90', 'PC'),
    ('Asus', 'T91', 'PC'),
    ('Acer', 'A22', 'Laptop'),
    ('Apple', 'PRO', 'Laptop'),
    ('Xerox', 'DL5564', 'Printer'),
    ('Xerox', 'DX62', 'Printer'),
    ('Canon', '2460', 'Printer'),
    ('Samsung', 'XL', 'Printer')
])

insert_pc([
    (0, 'T90', 4, 12, 120, '12x', 450),
    (1, 'T91', 2, 6, 240, '24x', 850),
    (2, 'A22', 4, 24, 540, '24x', 1200),
    (3, 'PRO', 2, 4, 120, '24x', 599)
])

insert_laptop([
(0,'T90',4,12,120,15,120),
(1,'T91',2,6,240,17,750),
(2,'A22',4,24,540,21,1850)
])

insert_printer([
(0,'DL5564','y','Laser', 210),
(1,'DX62','n','Laser', 250),
(2,'2460','n','Matrix', 546),
(3,'XL','y','Jet', 111)
])

select("SELECT model, speed, hd FROM PC WHERE price < 500")
select("SELECT DISTINCT maker FROM Product WHERE \"type\" = 'Printer'")
select("SELECT model, ram, screen FROM Laptop WHERE price > 1000")
select("SELECT * FROM Printer WHERE color = 'y'")
select("SELECT model, speed, hd,cd,price FROM PC WHERE price < 600 AND (cd = '12x' OR cd = '24x')")