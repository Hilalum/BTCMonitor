import requests
from datetime import datetime
from concurrent import futures
import time
import json
import sqlite3


from Include.Controller import server
from Include.Sqllite import init_sql
from Include.Monitor import *
if __name__ == '__main__':
    init_sql()
    server.run(port=8888, debug=True)
    timer(5)

