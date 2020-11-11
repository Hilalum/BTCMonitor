import sqlite3
from Include.GlobalValues import price
def init_sql():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE if not exists BTC
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
    conn.commit()
    conn.close()
def insert_register(USERNAME, TAX,WEEKMONEY,EMAIL,PASSWORD):
    conn = sqlite3.connect('test.db')
    BASE=price.get()
    c = conn.cursor()
    c.execute("INSERT INTO BTC (USERNAME, BASE,WEEKMONEY,EMAIL,PASSWORD,TAX) VALUES ('%s', '%s','%s','%s','%s','%s');"%(USERNAME,BASE,WEEKMONEY,EMAIL,PASSWORD,TAX))
    conn.commit()
    conn.close()