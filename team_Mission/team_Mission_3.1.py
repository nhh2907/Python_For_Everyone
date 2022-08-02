import sys

# 구구단 실행 함수
def timestable(n_times):
	print(f'{n_times} 단')
	for i in range(1, 10):
		result = n_times * i
		if result > 50:
			break
		print(f'{n_times} x {i} = {result}', sep='\n')

try:
	inp = int(input('What times table do you want? '))

	# 1에서 9 범위 값이 아니면 종료
	if not inp in range(1, 10):
		print('Must be between 1 and 9', 'Try again', sep='\n')
		sys.exit()
except ValueError:
	print('Must be a number', 'Try again', sep='\n')
else:
	# 함수 호출
	timestable(inp)
