# 2월 윤달은 고려하지 않고 28일 하나만 생각함
def calculate_100_day(m, d, dow, n):
	week = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun'] 
	cal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

	# 요일
	slice_week = week[week.index(dow):] + week[:week.index(dow)]
	
	# 날짜
	total_days = sum(cal[:(m-1)]) + d + (n-1)  # 총일수
	total_days = total_days % 365
	count = 0
	for i in cal:
		if total_days > 0:
			total_days = total_days - i
			count += 1
		else:  # total_days 변수가 음수가 되면 마지막에 뺀 달의 일수 다시 더하기
			total_days = total_days + cal[count - 1]
			break

	print(f'{m}월 {d}일 {dow}부터 {n}일 뒤는', \
		f'{count}월{total_days}일 {slice_week[(n % 7) -1]}')
	
# dow(요일): day of the week
month, day, dow = 1, 21, 'Fri'
after_day = 100 

calculate_100_day(month, day, dow, after_day)
