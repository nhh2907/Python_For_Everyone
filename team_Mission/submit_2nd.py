니얀 코딩코치님 6팀 2주차 팀미션 제출합니다

Q1)
def game_RPC(mine):
    import random

    # 리스트로'가위 바위 보' 생성
    list = ['rock', 'scissors', 'paper']

    # 컴퓨터 입력값 저장
    computer = random.randint(0, 2)

    # 사용자와 컴퓨터의 입력값 출력
    print('Computer:', list[computer])
    print('You:', list[mine], end='\n\n')

    # 가위바위보 승자 확인
    if mine == computer:
        print('Result : Draw!')
    elif mine == 0 and computer == 1:
        print('Result : You are win!')
    elif mine == 1 and computer == 2:
        print('Result : You are win!')
    elif mine == 2 and computer == 0:
        print('Result : You are win!')
    else:
        print('Result : Computer is win!')


def retry():
    while True:
        again = input('One more game?(yes or no): ')
        if again == 'yes':
            return True
        elif again == 'no':
            return False
        else:
            print('Input is wrong. Type must be yes or no')
            continue


while True:
    # 사용자의 입력값이 숫자이며 숫자가 아니면 오류 출력
    try:
        mine = int(input('0 for rock, 1 for scissors, 2 for paper: '))
        if not mine in [0, 1, 2]:
            print('Input must be between 0 and 2 \nTry again!')
            continue

        game_RPC(mine)

        # 게임 다시하기 묻기
        if retry():
            continue
        break
    except:
        print('Inputs must be a number. Try again')
        continue


Q2)
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


Q3)
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


Q4)
# 요금 테이블 함수 정의
def bus_fare(age, pay_type):
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
        continue

# 지불 방법 및 오류 검증
while True:
    pay_type = input('Preferable payment type(cash or card)? ')
    if pay_type != 'cash' and pay_type != 'card':
        print('Wrong input.\nWrite "cash" or "card" again')
        continue
    break

# 요금 테이블  함수 호출
bus_fare(age, pay_type)