

import trilateration
import database
import time
from numpy import *
from database import DistanceDatabase


_P1 = array([0, 0])
_P2 = array([2, 0])
_P3 = array([0, 2])

test = trilateration.Trilateration(_P1, _P2, _P3)
db = DistanceDatabase();
i = 0;
db.SelectDatabase()

'''
while(True):
    #get Db
    #test.Calculate(1.414*i,i,i)
    db.InsertDatabase("123456781", 2, 1.89)
    db.InsertDatabase("123456782", 2, 2.89)
    db.InsertDatabase("123456783", 2, 3.89)
    i+=1
    time.sleep(1)
    '''
    