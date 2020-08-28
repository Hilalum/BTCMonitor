import sqlite3
from Start import price
def insert_register(USERNAME, TAX,WEEKMONEY,EMAIL,PASSWORD):
    conn = sqlite3.connect('test.db')
    BASE=price
    c = conn.cursor()
    c.execute("INSERT INTO BTC (USERNAME, BASE,WEEKMONEY,EMAIL,PASSWORD,TAX) VALUES (%s, %s,%s,%s,%s,%s');"%(USERNAME,BASE,WEEKMONEY,EMAIL,PASSWORD,TAX))
    conn.commit()
    conn.close()