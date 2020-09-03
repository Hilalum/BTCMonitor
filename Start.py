import threading
from Include.Controller import server, flask_run
from Include.Sqllite import init_sql
from Include.Monitor import *
if __name__ == '__main__':
    init_sql()
    t = threading.Thread(target=price_monitor,args=())
    t.setDaemon(True)
    t.start()
    flask_run(8888, True)

