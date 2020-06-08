# 싱글톤 패턴 사례 1

import sqlite3


class MetaSingleton(type):
    _instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]
    

class Database(metaclass=MetaSingleton):
    connection = None
    
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj


db1 = Database()
db1.connect()

db2 = Database()
db2.connect()

print("Database Objects BD1 ", db1)
print("Database Objects BD2 ", db2)
