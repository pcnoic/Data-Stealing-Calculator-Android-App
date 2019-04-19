#!/usr/bin/python3

import copy 
import PyMySQL 
import cgi 
import cgitb 
import os
import sys
import sleep

if __name__='__name__':
  print('Content-type:text/html\n\n') 
  print('Starting connection to the database') 
  
  sleep.time(3) 
  
  #getting database credentials 
  usr = input('Please, enter DB username: ')
  dbname = input('Enter, DB name: ')
  dbpass = input('Enter, DB password: ') 
  dbsrv = input('Enter, database address: ') 
  
  
  
  try:
    con = PyMySQL.connect(dbsrv, usr, dbpass, dbname) 
    cursor = con.cursor() #initiating the cursor 
    idq = 4 
    name = "test" #enter your name 
    sqlQ1 = "INSERT INTO data(id, name) VALUES ('%d','%s')" %(idq, name)
   except: 
    print('cannot connect to sql, exiting...')
    sleep.time(5)
    exit()
    
    
   #trying to execute SQL script 
  try:
    cursor.execute(sqlQ1) #execution 
    con.commit() #commiting changes 
    print('ADDED') 
   except: 
    con.rollback() #revert changes in case of failure 
   
  
  con.close() 
  
  
    