total = 0.0
count = 0

while True:
	val = input('Enter a number ')
	if val == 'done':
		if count == 0:
			quit()
		break
	try:
		fval = float(val)
	except:
		print('Invalid input')
		continue
	count = count + 1
	total = total + fval

print(f'Total : {total}\nCounting : {count}\nAverage : {total/count}')
