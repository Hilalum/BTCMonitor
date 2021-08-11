import sqlite3
from Include.GlobalValues import price

db_name = 'test.db'

def init_sql():
   execute_sql('''CREATE TABLE if not exists BTC
           (ID integer PRIMARY KEY autoincrement,
           USERNAME           TEXT    NOT NULL,
           MONEY            INT,
           BASE        INT,
           BTC         LONG,
           TAX         LONG,
           WEEKMONEY   INT,
           EMAIL       TEXT,
           PASSWORD    TEXT
           );''')

def insert_register(USERNAME, TAX, WEEKMONEY, EMAIL, PASSWORD):
    BASE = price.get()
    execute_sql(
        "INSERT INTO BTC (USERNAME, BASE,WEEKMONEY,EMAIL,PASSWORD,TAX) VALUES ('%s', '%s','%s','%s','%s','%s');" % (
            USERNAME, BASE, WEEKMONEY, EMAIL, PASSWORD, TAX))


def update(USERNAME, TAX, WEEKMONEY, EMAIL, PASSWORD):
    execute_sql(
        "UPDATE BTC set WEEKMONEY = '%s',EMAIL= '%s',TAX='%s' where USERNAME = '%s' and PASSWORD = '%s';" % (
            WEEKMONEY, EMAIL, TAX, USERNAME, PASSWORD))


def execute_sql(sql):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    conn.close()