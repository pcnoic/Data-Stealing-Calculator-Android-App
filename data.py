#!C:/Python27

import copy
import mysql.connector
import cgi
import cgitb
import os
import sys



if __name__ == '__main__':
    print "Content-type:text/html\n\n"
    conn = mysql.connector.connect(user='root',password='',host='localhost',database='abcd')
    cursor = conn.cursor()
    idq=4
    name="aryan"
    sql1 = "INSERT INTO data(id,name) VALUES ('%d','%s')" %(idq,name)
    print sql1


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

