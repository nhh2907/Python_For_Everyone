# 가위바위보 게임 함수
def play_rcp(n):
	import random
	
	count = [draw:=0, win:=0, lose:=0]
	# count를 아래처럼 선언 및 초기화해도 됨
	# 왈라 operator는 가독성이 좋지않아 지양하는 것이 좋다
	# count =[0] * 3
	table = ['draw', 'win', 'lose']
	# 딕셔너리의 변수 이름은 <키 명사 복수형>_to_<값 명사 복수형> 형태로 하는 것이 좋다
	# rcp_nums_to_options = {0:'scissor', 1:'rock', 2:'paper'}
	rcp = {0:'scissor', 1:'rock', 2:'paper'}
	i = 0

	while i < n:
		inp = input('0 for scissor, 1 for rock, 2 for paper ')
		if not inp in ['0', '1', '2'] + list(rcp.values()):
			print('Enter 0, 1, 2, scissor, rock or paper')
			print('Try again')
			continue

		# 딕셔너리의 값으로 키값 알아내기
		# 아래 if 둘 중 아무거나 사용해도 됨
		# if inp in ['scissor', 'rock', 'paper']:
		if inp in list(rcp.values()):
			for key, value in rcp.items():
				if value == inp:
					user = key
		else:
			# if에서 inp이 'scissor', 'rock', 'paper' 중 하나인지를 확인하는 것 대신
			# inp.isdigit()으로 먼저 체크하고 거짓이면 문자열 scissor', 'rock', 'paper'를 체크하는 것이 좋다
			# 위의 방법이  guard clause임
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
