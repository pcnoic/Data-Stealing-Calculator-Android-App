#!/usr/bin/python3 

import cgi 
import cgitb 
import os
import PyMySQL 
import datetime 
import time
import json
import sys 

usr = input('Please, enter DB username: ')
dbname = input('Enter, DB name: ')
dbpass = input('Enter, DB password: ') 
dbsrv = input('Enter, database address: ') 


try:
  con = PyMySQL.connect(dbsrv, dbname, dbpass, dbname) #attempoting connection to SQL 
  cursor = con.cursor() 
  
  query = "SELECT * FROM DATA ORDER BY NAME ASC" 
  
  cursor.execute(query) 
  results = cursor.fetchall() 
  
  listUNO = []
  
  for row in results:
    name = row[1] 
    print name 
    
   
  con.commit() #commiting to database 
  con.close() #exiting 
  
  
  
  
  
  
