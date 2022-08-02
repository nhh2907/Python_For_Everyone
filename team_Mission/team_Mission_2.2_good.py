# 다음 코드는 if문 없이 이진 탐색 모듈bisect의 bisect() 메써드로 구현함
def calculate_aftertax(mon):
	import bisect
	
	pretax_yearly = mon * 12

	# 세전 연봉에 따른 세율 구간표
	table = [1200, 4600, 8800, 15000, 30000, 50000]
	tax_rate = [0.06, 0.15, 0.24, 0.35, 0.38, 0.40, 0.42]

	# 이진 탐색 함수로 리스트에 삽입할 위치의 인덱스 찾기
	index = bisect.bisect_left(table, pretax_yearly)

	aftertax_yearly = pretax_yearly - pretax_yearly*tax_rate[index]

	print(f'Pretax yearly payment = {pretax_yearly}')
	print(f'Aftertax yearly payment = {aftertax_yearly}')
	
monthly_pay = int(input('Your monthly payment("만원"): '))
calculate_aftertax(monthly_pay)
