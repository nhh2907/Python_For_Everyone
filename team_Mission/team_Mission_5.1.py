import random

# Error가 있으면 True, 없으면 False
def check_input_error(user_input, largest):
	length_input = user_input.split()
	was_space = 1
	i = 0

	# 입력한 숫자들이 3개 이하인지 확인
	if len(length_input) > 3:
		print('Maximum number is three')
		return True
	
	# 입력한 수들은 1씩 증가하며 연속된 숫자들이어야 함
	while i < len(length_input)-1:
		if int(length_input[i+1]) != int(length_input[i]) + 1:
			print('Numuber should be consecutive!')
			return True
		i += 1	

	# 숫자 사이에 빈칸 한 개만 존재하는지 확인
	# 숫자 외의 문자가 입력됐는지 확인
	for character in user_input:
		if character == ' ':
			was_space += 1
		elif character.isdigit() and was_space == 0:
			pass
		elif character.isdigit() and was_space == 1:
			was_space = 0
		elif was_space > 1 or character not in range(0, 10):
			print('Input is incorrect')
			print('Only numeric numbers are allowed')
			print('Only one space is allowed between numbers')
			print('Try again')
			return True

	return False

def play_31game():
	largest = 0

	while largest < 31:
		user_input = input('You? ')
		computer_turn_num = random.randint(1, 3)

		# 입력 양식(포멧)을 지켰는지 확인
		if check_input_error(user_input, largest):
			continue

		# 사용자의 입력 첫번째 숫자는 컴퓨터의 마지막 숫자보다 1 커야함
		if int(user_input[:2]) != largest + 1:
			print('Input number must be one more than computer last number')
			continue
		
		# 입력값의 마지막 숫자를 largest 변수에 업데이트
		user_input = user_input.split()
		largest = int(user_input[-1])


		# 컴퓨터 입력 후 largest 변수 업데이트
		for i in range(computer_turn_num):
			if largest == 31:  # 유저 또는 컴퓨터가 31을 입력한 경우 나가기
				break
			largest += 1
			print(f'Computer: {largest}')

print('베스킨 라빈스 31 게임~')	
print('Enter one~three numbers with one space each') 
play_31game()
