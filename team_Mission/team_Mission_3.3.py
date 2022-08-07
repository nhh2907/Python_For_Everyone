def even_number(n, m):
	set_ = [i for i in range(n, m + 1)]

	# n과 m사이의 숫자들 중에 중앙값 인덱스 찾기
	mid = (m-n+1) // 2

	for num in set_:
		if num % 2 != 0:
			continue

		print(f'{num} (even)')
	
		# 조건1: 집합의 원소개수가 홀수인 경우이면서
		# 조건2: 집합의 짝수 원소 각각이 그 집합의 중앙값인지 판별
		if len(set_) % 2 != 0 and num == set_[mid]:
			print(f'{set_[mid]} (middle)')

n = int(input('first number: '))
m = int(input('second number: '))
print()

even_number(n, m)
