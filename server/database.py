
import sqlite3
from sqlite3 import datetime
from macpath import curdir

Debug = True

class DistanceDatabase:
    
    def __init__(self):
        #self.con = sqlite3.connect(':memory:')
        self.con = sqlite3.connect('test.db')
        cur = self.con.cursor()
        cur.execute('create table if not exists beacon (uuid string , minor int, distance double,regdate TIMESTAMP DEFAULT CURRENT_TIMESTAMP);')
    
    
    def InsertDatabase(self,uuid, minor, distance):
        quarry = "insert into beacon values(\'%s\',%d,%f,datetime('now','localtime'));"%(uuid,minor,distance)
        cur = self.con.cursor()
        cur.execute(quarry)
        self.con.commit()
        if(Debug == True):
            print quarry
    
    
    def SelectDatabase(self):
        cur = self.con.cursor()
        
        cur.execute('select * from beacon;')
        rdate =  cur.fetchone()[3]
        if(Debug == True):
            print rdate
            
        quarry = "SELECT * FROM beacon WHERE regdate LIKE \'%s\';"%rdate
        if(Debug == True):
            print quarry
        
        cur.execute(quarry);
        print cur.fetchall()
        