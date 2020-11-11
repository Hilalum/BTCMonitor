import threading
from Include.Controller import server, flask_run
from Include.Sqllite import init_sql
from Include.Monitor import *
from Include.GlobalValues import price
if __name__ == '__main__':
    init_sql()
    price.put(0)
    t = threading.Thread(target=price_monitor,args=(price,))
    t.setDaemon(True)
    t.start()
    flask_run(8888, True)

