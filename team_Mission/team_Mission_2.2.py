def yearly_payment(montly_payment):
	yearly = monthly_payment * 12

	if yearly <= 1200:
		after_tax = yearly * (1 - 0.06) 
	elif yearly <= 4600:
		after_tax = yearly * (1 - 0.15)
	elif yearly <= 8800:
		after_tax = yearly * (1 - 0.24)
	elif yearly <= 15000:
		after_tax = yearly * (1 - 0.35)
	elif yearly <= 30000:
		after_tax = yearly * (1 - 0.38)
	elif yearly <= 50000:
		after_tax = yearly * (1 - 0.40)
	else:
		after_tax = yearly * (1 - 0.42)

	print('Yearly_pay is', yearly, '만원입니다')
	print('After-tax-yearly_pay is', int(after_tax), '만원입니다')

while True:
	try:
		monthly_payment = int(input('How much money do you get monthly paid?(unit is "만원")\n'))
		break
	except:
		print('Input must be a number.\nTry again')
		continue

yearly_payment(monthly_payment)
