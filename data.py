#!C:/Python27

import copy
import mysql.connector
import cgi
import cgitb
import os
import sys
import sleep


if __name__ == '__main__':
    print "Content-type:text/html\n\n"
    print "Starting connection to the database" 
    sleep.time() 
    
    try:
		conn = mysql.connector.connect(user='root',password='',host='localhost',database='abcd')
		cursor = conn.cursor()
		idq=4
		name="christos"
		sql1 = "INSERT INTO data(id,name) VALUES ('%d','%s')" %(idq,name)
		print sql1
	except:
		# error message in case connection to sql is not available 
		print "cannot connect to sql. exiting..." 
		sleep.time(2) 
		exit() 
		
    try:
       # Execute the SQL command
       cursor.execute(sql1)
       # Commit your changes in the database
       conn.commit()
       print "added"
    except:
       # Rollback in case there is any error
       conn.rollback()


    conn.close()

