''' 다음 코드는 if문 없이 가위바위보 게임 코드를 구현했다 '''

import random

# 가위바위보 실행 함
def play_rcp(i, com):

	# 컴퓨터값과 나의 값과의 차이가 결과값이 되므로 인덱스 찾기
	index = i - com

	# 가위바위보를 저정하는 딕셔너리
	# 결과값을 담고 있는 리스트
	inputs = {0:'scissor', 1:'rock', 2:'paper'}
	result = ['draw', 'win', 'lose']

	print(f'You : {inputs[i]}, computer = {inputs[com]}')
	
	# 컴퓨터의 키값과 유저의 키값의 차이값을 리스트 인덱스로 넣음
	print(f'Yor are {result[index]}!')

while True:
	# 문자 검증
	try:
		user = int(input('0 = scissor, 1 = rock, 2 = paper: '))
	except ValueError:
		print('Inputs must be a number')
		continue
	
	# 0과 2 사이 숫자 입력 검증
	if not user in [0, 1, 2]:
		print('Input must be between 0 and 2')
		print('Try again')
		continue

	computer = random.randint(0, 2)
	break

play_rcp(user, computer)
