import requests
from datetime import datetime
from concurrent import futures
import time
import json
import sqlite3

# 每n秒执行一次
from Include.Controller import server
price = 0

def timer(n):
    while True:
        url = "https://sochain.com/api/v2/get_price/BTC/USD"
        res = json.loads(requests.get(url=url).text)
        if(res['status'].strip() == 'success'):
            for i in res['data']['prices']:
                if price == 0:
                    price = float(i['price'])
                else:
                    price = (price + float(i['price'])) / 2
        print(datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))
        print(price)
        time.sleep(n)
def sql():
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

if __name__ == '__main__':
    sql()
    server.run(port=8888, debug=True)
    timer(5)

