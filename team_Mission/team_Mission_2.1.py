def game_RPC(mine):
	import random

	# 리스트로'가위 바위 보' 생성
	list = ['rock', 'scissors', 'paper']
	
	# 컴퓨터 입력값 저장
	computer = random.randint(0,2)

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
