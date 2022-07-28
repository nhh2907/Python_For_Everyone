# 요금 테이블 함수 정의
# 함수 이름 동사로 시작
def calculate_bus_fare(age, pay_type):
	if age < 8:
		result = '무료'
	elif age < 14:
		result = '450 원'
	elif age < 20:
		if pay_type == 'card':
			result = '720 원'
		else:
			result = '1000 원'
	elif age < 75:
		if pay_type == 'card':
			result = '1200 원'
		else:
			result = '1300 원'
	else:
		result = '무료'

	print('Age =', age, '세')
	print('Pay_type =', pay_type)
	print('Bus_fare =', result)

# 나이 입력과 오류 검증
while True:
	try:
		age = int(input('What is your age? '))
		if age <= 0:
			print('Age must be over 0. Try again')
			continue
		break
	except:
		print('Input must be a number')
		# 무한 루프이므로 여기서 continue는 무의함
		# continue

# 지불 방법 및 오류 검증
while True:
	pay_type = input('Preferable payment type(cash or card)? ')
	if pay_type != 'cash' and pay_type != 'card':
		print('Wrong input.')
		print('Write "cash" or "card" again')
		continue
	break
			
# 요금 테이블  함수 호출
calculate_bus_fare(age, pay_type)
