#!/usr/bin/python3

import pymysql.cursors
import pymysql

def createtable():

	# Open database connection
	db = pymysql.connect("localhost","root","","counselor" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# Drop table if it already exist using execute() method.
	cursor.execute("DROP TABLE IF EXISTS usermsg")

	# Create table as per requirement
	sql = """CREATE TABLE usermsg (
	   message  VARCHAR(100))"""

	cursor.execute(sql)

	# disconnect from server
	#db.close()