print 'sum all the input'
temp = []
sum = 0
while True:
	print 'input your num'
	a = raw_input()
	try:
		if a == 'q' :
			for i in temp :
				sum = sum + i
			print 'the sum of the num is: {}'.format(sum)
			break
		else:
			aa = float(a)
			temp.append(aa)
	except:
		print 'you should only input num or "q", please input again'
import os
os.system("pause")