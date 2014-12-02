# test BLE Scanning software
# jcs 6/8/2014

import blescan
import sys
import sqlite3
import math
import time

DEBUG = True

import bluetooth._bluetooth as bluez

def calculateAccuracy(txPower, rssi): #http://stackoverflow.com/questions/20416218/understanding-ibeacon-distancing
	if (rssi == 0):
		return -1.0; # if we cannot determine accuracy, return -1.

	ratio = rssi*1.0/txPower;
	if (ratio < 1.0): 
		return math.pow(ratio,10);
	else: 
		accuracy =  (0.89976)*math.pow(ratio,7.7095) + 0.111;    
		return accuracy;



dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print "ble thread started"

except:
	print "error accessing bluetooth device..."
	sys.exit(1)
	
#con = sqlite3.connect(':memory:')
con = sqlite3.connect('test.db')
cur = con.cursor()
cur.execute('create table if not exists beacon (mac string, uuid string,  major int, minor int, distance double,regdate TIMESTAMP DEFAULT CURRENT_TIMESTAMP);')

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

while True:
	returnedList = blescan.parse_events(sock, 1)
	n = len(returnedList)
	now = time.localtime()
	if( n > 5 ):
		acc =  calculateAccuracy(returnedList[4], returnedList[5])
		#print "distance :", acc 
		
		mac = returnedList[0]
		uuid = returnedList[1]
		major = returnedList[2]
		minor = returnedList[3]
		txpower = returnedList[4]
		rssi = returnedList[5]
		
		#print mac, uuid, major, minor, txpower, rssi
		
		quarry = "insert into beacon values(\'%s\',\'%s\',%d,%d,%f,datetime('now','localtime'));"%(mac,uuid,major,minor,acc)
		print quarry, rssi,now.tm_min, now.tm_sec
		cur.execute(quarry);
		cur.execute('select * from beacon;')
		#for record in cur:
		#	print(record)
		con.commit()
	else:
		print "error"
	