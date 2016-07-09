#!C:/Python27/python


import cgi
import cgitb
import os
import mysql.connector
import datetime
import time
import json
import sys




conn = mysql.connector.connect(user='root',password='',host='localhost',database='abcd')

cursor = conn.cursor()
sql="select * from data order by name asc"
cursor.execute(sql)
results = cursor.fetchall()
list1=[]
for row in results:
         name = row[1]
         print name
         

conn.commit()
conn.close()








