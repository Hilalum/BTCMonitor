
from Include.Controller import server
from Include.Sqllite import init_sql
from Include.Monitor import *
if __name__ == '__main__':
    init_sql()
    server.run(port=8888, debug=True)
    price_monitor(5)

