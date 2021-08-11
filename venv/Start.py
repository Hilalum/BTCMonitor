import threading
from Include.Controller import server, flask_run
from Include.Sqllite import init_sql
from Include.Monitor import *
from Include.GlobalValues import price
if __name__ == '__main__':
    init_sql()
    flask_run(8888, True)
    t = threading.Thread(target=price_monitor)
    t.setDaemon(True)
    t.start()

