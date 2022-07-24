def grader(name, score):
	if score >= 95:
		grade = 'A+'
	elif score >= 90:
		grade = 'A-'
	elif score >= 85:
		grade = 'B+'
	elif score >= 80:
		grade = 'B-'
	elif score >= 75:
		grade = 'C+'
	elif score >= 70:
		grade = 'C-'
	elif score >= 65:
		grade = 'D+'
	elif score >= 60:
		grade = 'D-'
	else:
		grade = 'F'
	
	print('Your name = ', name)
	print('Your score = ', score, '점')
	print('Your grade = ', grade)

# 이름 입력
name = input('What is your name? ')

# 점수 입력과 오류 검증
while True:
	try:
		score = int(input('What score did you get? '))
		if score > 100 or score < 0:
			print('the scope of score is between 0 to 100\nTry again')
			continue
		break
	except:
		print('Input must be a number')
		continue

# 그레이드 함수 실행 및 출력
grader(name, score)
