# Wrong(잘못된 것)이 있으면 True, 없으면 False
def check_wrong(e):
	# 전화번호가 숫자와 대쉬 문자로만 이루어졌는지 확인
	for i in e[1]:
		if not i.isdigit() and i != '-':
			return True
	
	# 위의 조건을 만족했으면 다음 추가 조건에 부합하는지 확인
	if (
		e[1].startswith('010')
		and len(e[1]) == 13
		and e[1].count('-') == 2
		and e[1][3] == '-'
		and e[1][8] == '-'
	):
		return False

	return True

def check_guest_wrong_numbers(guest_book):
	list_guests = guest_book.split()

	fh = open('right_guest_book.txt', 'w')
	for one_guest in list_guests:
		e = one_guest.split(',')	
		if check_wrong(e):  # Wrong(잘못된 것)이 있으면 True, 없으면 False
			fh.write(f'잘못 쓴 사람: {e[0]}\n')
			fh.write(f'잘못 쓴 번호: {e[1]}\n') 
			fh.write('\n')
	fh.close()

guest_book = """ 김갑,123456789
이을,010-1212-5418
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333 """

check_guest_wrong_numbers(guest_book)
