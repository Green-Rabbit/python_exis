import sqlite3
conn = sqlite3.connect('C:\Users\Y\Desktop\python_exis\mytest.db')
cursor = conn.cursor()
print ('Input some students')
while True:
	name = raw_input("student's name: ")
	username = raw_input("student's username: ")
	id_num = raw_input("student's id number: ")
	sql1 = ''' insert into students
			( name ,username ,id )
			values
			(:Name, :User, :Id)'''
	cursor.execute(sql1,{'Name':name ,'User':username ,'Id':id_num })
	conn. commit()
	cont = raw_input('Another student?')
	if cont.lower() == 'n' :
		break
cursor.close()
import os
os.system("pause")