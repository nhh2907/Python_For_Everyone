# 함수 이름은 동사로 시작하는게 좋다
def calculate_yearly_payment(montly_payment):
	yearly = monthly_payment * 12

	if yearly <= 1200:
		tax_rate = 0.06 
	elif yearly <= 4600:
		tax_rate = 0.15
	elif yearly <= 8800:
		tax_rate = 0.24 
	elif yearly <= 15000:
		tax_rate = 0.35 
	elif yearly <= 30000:
		tax_rate = 0.38 
	elif yearly <= 50000:
		tax_rate = 0.40 
	else:
		tax_rate = 0.42 

	after_tax = yearly * (1 - tax_rate)
	print('Yearly_pay is', yearly, '만원입니다')
	print('After-tax-yearly_pay is', int(after_tax), '만원입니다')

while True:
	try:
		monthly_payment = int(input('How much money do you get monthly paid?(unit is "만원")\n'))
		break
	except ValueError:
		# 중간에 개행문자 넣는것보다 프린트함수 두번 사용이 가독성좋다.
		print('Input must be a number.')
		print('Try again')

calculate_yearly_payment(monthly_payment)
