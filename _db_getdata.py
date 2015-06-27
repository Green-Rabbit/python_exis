import sqlite3
conn = sqlite3.connect('C:\Users\Y\Desktop\python_exis\mytest.db')
cursor = conn.cursor()
#sql = "select * from students"
sql = "select name from students"
results = cursor.execute(sql)
all_students = results.fetchall()
for student in all_students:
	print student
cursor.close()
import os
os.system("pause")