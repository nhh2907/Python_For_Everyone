# 윤년, 그레고리력 근거하여 구함
def leap_year(y):
      # 4의 배수이며 100의 배수가 아닐 때 and 400의 배수일 때
      if ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0):
          return True
      else:
          return False

def check_valid_day_number(year, month, day):
	# 해당 달의 일수(num)
	num = 31
	if month in [4, 6, 9, 11]:  # 4, 6, 9, 11월은 30일
		num = 30
	if month == 2:  # 2월은 윤년 판별에 따라 29일 또는 28일로 나눈다
		if leap_year(year):
			num = 29
		else:
			num = 28
	
	# 일수가 해당 달의 일수를 넘는지 확인
	if day > num:
		return True
	else:
		return False

def calculate_d_day(y, m, d, dow, n):
	dow.lower().capitalize()
	week = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun'] 

	# 요일
	# 기준요일(dow)을 새 리스트의 0번지에 놓음
	slice_week = week[week.index(dow): ] + week[ :week.index(dow)]
	
	# 날짜
	for _ in range(n):
		d += 1
		if check_valid_day_number(y, m, d):
			d = 1
			m += 1 
			if m > 12:
				m = 1 
				y += 1
	
	# 요일: 시작하는 첫 날을 포함해야 하므로 1일 빼야함
	# (n - 1) % 7도 가능함:
	#	설명1: 월요일부터 일요일까지 개수는 7개
	#   설명2: 월요일부터 일요일까지 사이 개수는 6개
	print(f'{y}년 {m}월 {d}일 {slice_week[(n % 7) - 1]}') 
	#print(f'{y}년 {m}월 {d}일 {slice_week[(n - 1) % 7]}') 
	
year, month, day, after_day = input(f"Enter Today 'year' 'month' 'day' 'after day: ").split()
dow = input('What day of week is today?(mon, tue, wed, thur, fri, sat, sun) ').lower().capitalize()

print(f'현재 날짜: {year}년 {month}월 {day}일 {dow}요일.', f'{after_day}일 이후는?')

# day를 하루 빼서 넘겨주는 이유
# -> 시작하는 날을 포함해야 하기 때문에 함수 안에서 d += 1을 카운트할 때
#   d의 값은 하루 전날이어야 함

# 질문:
# 아래 함수호출 인자들 하나하나 int()로 해줬는데 한 번에 해줄 수 있는 방법이 있을까요?
calculate_d_day(int(year), int(month), int(day)-1, dow, int(after_day))
