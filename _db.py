import sqlite3
conn = sqlite3.connect('C:\Users\Y\Desktop\python_exis\mytest.db')
cursor = conn.cursor()
sql = ''' create table students(
		name text,
		username text,
		id int)'''
cursor.execute(sql)
cursor.close()
