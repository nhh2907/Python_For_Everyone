# 가위바위보 게임 함수
def play_rcp(n):
	import random
	
	count = [draw:=0, win:=0, lose:=0]
	table = ['draw', 'win', 'lose']
	rcp = {0:'scissor', 1:'rock', 2:'paper'}
	i = 0

	while i < n:
		inp = input('0 for scissor, 1 for rock, 2 for paper ')
		if not inp in ['0', '1', '2', 'scissor', 'rock', 'paper']:
			print('Enter 0, 1, 2, scissor, rock or paper')
			print('Try again')
			continue

		# 딕셔너리의 값으로 키값 알아내기
		if inp in ['scissor', 'rock', 'paper']:
			for key, value in rcp.items():
				if value == inp:
					user = key
		else:
			user = int(inp)

		computer = random.randint(0, 2)
		index = user - computer
		count[index] += 1

		print(f'You : {rcp[user]}')
		print(f'Computer : {rcp[computer]}')
		print(f'{i+1} game! You are {table[index]}', '\n')

		i += 1

	# 게임종료 후 전적 출력
	print(f'Your Total: {count[1]} win, {count[0]} draw, {count[2]} lose')
	print(f'Computer Total: {count[2]} win, {count[0]} draw, {count[1]} lose')

# 횟수 입력 및 오류 검증
while True:
	try:
		n = int(input('How many games? '))
		if not n > 0:
			print('A number must be over 0')
			continue
		break
	except ValueError:
		print('Must be a number')

# 가위바위보 함수 호출
play_rcp(n)
