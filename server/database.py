
import sqlite3
from sqlite3 import datetime
from macpath import curdir


class database:
    
    def __init__(self):
        self.con = sqlite3.connect(':memory:')
        #con = sqlite3.connect('test.db')
        self.cur = self.con.cursor()
        self.cur.execute('create table if not exists beacon (uuid string , minor int, distance double,regdate TIMESTAMP DEFAULT CURRENT_TIMESTAMP);')

    
    
    def InsertDatabase(self,uuid, minor, distance):
        self.quarry = "insert into beacon values(\'%s\',%d,%f,datetime('now','localtime'));"%(uuid,minor,distance)
        print self.quarry
    
    
    
    def SelectDatabase(self, datetime):
        self.cur.execute(self.quarry);
        self.cur.execute('select * from beacon;')
        #for record in cur:
        #    print(record)
