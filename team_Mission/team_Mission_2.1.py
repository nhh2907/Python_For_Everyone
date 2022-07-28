# 함수 이름은 snake_case로 써주세요. (대문자 X)
# 함수 이름은 동사로 시작하는 게 좋다. (game_RPC -> play_game)

def play_game(mine):
	from random import randint 

	# 리스트로'가위 바위 보' 생성
	# 파이썬에서 'list'는 키워드(예약어)이므로 변수이름 사용X
	# 키워드를 피하기 위해 변수이름에 underscore를 붙여 사용함
	list_ = ['rock', 'scissors', 'paper']
	
	# 컴퓨터 입력값 저장
	computer = randint(0,2)

	# 사용자와 컴퓨터의 입력값 출력
	print('Computer:', list_[computer])
	print('You:', list_[mine], end='\n\n')

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
			# 여기서 continue는 의미가 없다. 무한 루프이므로
			# continue	
		
while True:

	# 사용자의 입력값이 숫자이며 숫자가 아니면 오류 출력
	# except로 에러를 잡을 때는 except로 모든 에러를 잡는건 좋지 않다
	# 'except ValueError'와 같이 구체적인 에러를 명시가 낫다
	try:
		mine = int(input('0 for rock, 1 for scissors, 2 for paper: '))
		if not mine in [0, 1, 2]:
			print('Input must be between 0 and 2')
			print('Try again!')
			continue
		
		play_game(mine)
	
		# 게임 다시하기 묻기
		if retry():
		    continue
		break
	except ValueError:
		print('Inputs must be a number. Try again')
