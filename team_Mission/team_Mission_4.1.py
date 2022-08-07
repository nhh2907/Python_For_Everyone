def make_comma(number):

	count = 0
	n = len(number)
	comma_list = []

	while n != 0:
		comma_list.append(number[n-1])  # 마지막 인덱스의 수부터 리스트 삽입
		count += 1

		# 조건 1 : 세자리수마다 콤마를  리스트 삽입
		# 조건 2 : 마지막 자리수가 아닌 경우에만 리스트 삽입
		if count == 3 and n != 1:
			comma_list.append(',')
			count = 0
		
		n -= 1

	comma_list.reverse()
	
	for i in comma_list:
		print(i, end='')

	print()

user_input = input('Enter a number to be seperated by comma: ')
make_comma(user_input)
