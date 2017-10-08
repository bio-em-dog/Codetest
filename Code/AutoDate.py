month=1
day=0
for i in range(0,365,1):
	day=day+1
	if day<10:
		if month<10:
			print("2018"+".0"+str(month)+".0"+str(day))
		else:
			print("2018"+"."+str(month)+".0"+str(day))
	else:
		if month<10:
			print("2018"+".0"+str(month)+"."+str(day))
		else:
			print("2018"+"."+str(month)+"."+str(day))

#	print ('-')
#	print ('-')
#	print ('-')
#	print ('-')

	if day==31 and (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
		day=0
		month=month+1
	elif day==30 and (month==4 or month==6 or month==9 or month==11):
		day=0
		month=month+1
	elif day==28 and month==2:
		day=0
		month=month+1

a=["周日","周一",'周二','周三','周四','周五','周六']
for i in range(0,365,1):
#	string=(open('python_temp_test.py')).readlines()
	print(string[i][0:10]+a[i%7]+'\n\n')