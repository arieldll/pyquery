import psycopg2
import datetime

class TConnection:
    def __init__(self, host, port, user, password, database):
        self.connection = None
        try:
            self.connection = psycopg2.connect(user = user, password = password, host = host, port = port, database = database)
        except Exception as e:
            print('Cannot connect to database due ' + str(e))
    
    def conn(self):
        return self.connection
        
