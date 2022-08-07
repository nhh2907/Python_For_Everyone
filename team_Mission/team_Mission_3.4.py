def eratos_sieve(n, m):
	# 인덱스와 배열의 수를 일치시킴
	prime_list = [True for i in range(m+1)]
	count = 0
	# 배수로 소거할 때 마지막 범위를 제곱근까지만 해도 나머지 배수 전부 소거함
	m_sqrt = int(m**0.5)

	# 에라토스테네스의 체
	for i in range(2, m_sqrt+1):
		if prime_list[i] is True:	# if prime_list[i]로 해도 됨
			for j in range(i+i, m+1, i):  # i의 다음 배수부터 배수 삭제
				prime_list[j] = False

	# prime_list에서 index n부터(단 0, 1 제외) 끝까지 True 갯수 counting
	for i in prime_list[n:m+1]:		# for i in prime_list[n:]: 이렇게도 가능
		if i is True:				# if i: 이렇게도 가능
			count += 1

	# n(최소 2)부터 m까지 소수 부분만 slicing
	sieve = [i for i in range(n, m+1) if prime_list[i] is True]  # is_True는 없어도 됨
	
	print(prime_list[2:m+1])
	print('Prime list: ', sieve)
	print('The total of prime numbers is', count)

# 소수는 2부터 시작이므로 2이상 입력을 받아야 함
while True:
	try:
		n = int(input('first number: '))
		m = int(input('second number: '))
		if not (n >= 2 and m >= 2):
			print('Prime number must be at least 2', 'Try again', sep='\n')
			continue
		break
	except ValueError:
		print('Enter a number', 'Try again')

eratos_sieve(n, m)
