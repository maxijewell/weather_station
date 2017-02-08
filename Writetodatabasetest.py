#!/usr/bin/env python

import MySQLdb

db = MySQLdb.connect("localhost", "monitor", "*****", "weather_readings")

curs=db.cursor()

try:
	curs.execute ("INSERT INTO readings VALUES(NOW(), 15, 1000)")
	curs.execute ("INSERT INTO readings VALUES(NOW() - INTERVAL 12 HOUR, 15, 1000)")
	curs.execute ("INSERT INTO readings VALUES(NOW() - INTERVAL 1 DAY, 15, 1000)")

	db.commit()
	print "Data committed"

except:
	print "Error: the database is being rolled back"
	db.rollback()
