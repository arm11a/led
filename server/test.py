'''
Created on Oct 27, 2014

@author: sraven
'''

import sqlite3

con = sqlite3.connect(':memory:')
cur = con.cursor()
cur.execute('create table t1 (c1 int, c2 int);')
cur.execute('insert into t1 values(1,1);')
cur.execute('insert into t1 values(2,2);')
cur.execute('select * from t1;')

for record in cur:
    print(record)

con.commit()


