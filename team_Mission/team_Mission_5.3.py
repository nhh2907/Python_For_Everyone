def guess_number():
	import random

	# 컴퓨터 난수 3개 생성(중복 불가)
	list_com = list()
	i = 0
	while i < 3:
		com_number = random.randint(0, 100)
		if com_number in list_com:
			continue

		list_com.append(com_number)
		i += 1

	list_com.sort()
	print(list_com)

	# 사용자의 숫자 맞추기
	count = 0
	num_answer = 0
	list_user = list()
	while num_answer != 3:
		try:
			user = int(input('숫자를 예측해보세요: '))
			if user in list_user:
				print('이미 예측에 사용한 수입니다')
				continue
			list_user.append(user)
			count += 1
			print(f'{count}차 시도')
		except ValueError:
			print('Input is number')
			continue

		if count == 5:
			print(f'Hint: 최소값은 {list_com[0]//10} 십대')
		elif count == 10:
			print(f'Hint: 최대값은 {list_com[2]//10} 십대')
			
		types = ['최소값', '중간값', '최대값']

		if user in list_com:
			index = list_com.index(user)
			print(f'-> 숫자를 맞추셨습니다!! {types[index]}은 {user}')
			num_answer += 1

	print('Game is finished')

guess_number()
