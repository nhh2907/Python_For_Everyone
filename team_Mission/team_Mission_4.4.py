# Step 1: 주민번호 양식 오류 체크
# Step 2: 뒷자리 성별 오류 검증
# ... 00~21으로 시작하면 2000년대생인지 1900년대생인지 물어보기. 2000년대생이면
# ... 뒷자리 3 또는 4로 시작해야 함. 1900년대생은 뒷자리 1 또는 2로 시작함
# Step 3: 출력

def check_id_format(id_user):
	scope = [str(i) for i in range(0, 5)]
	
	# 주민등록번호가 숫자와 대쉬로만 되어있는지 확인
	for i in id_user:
		if not i.isdigit() and i != '-':
			return False

	# 추가 조건 확인
	if len(id_user) != 14 \
		or id_user[2] not in scope[:2] \
		or id_user[4] not in scope[:5] \
		or id_user.count('-') != 1 \
		or id_user[6] != '-' \
		or id_user[7] not in scope[1:]:
		return False
	
	return True

def check_sex_index(id_user):
	number = [str(i) for i in range(0, 10)]
	ox_numbers = {'X':0, 'O':1}
	flag = 0  #1900년대생: 0, 2000년대생: 1

	# 00~21로 시작하면 2000년대생인지 1900년대생인지 flag에 저장
	if (id_user[0] in number[:2] and id_user[1] in number[:]) \
		or (id_user[0] == number[2] and id_user[1] in number[:2]):
		answer = input("Enter 'O' if 2000's, 'X' if 1900's: ").upper()
		flag = ox_numbers[answer]
	
	# 2000년대생인데 뒷자리가 3,4가 아니면 오류
	# 1900년대생인데 뒷자리가 1,2가 아니면 오류
	if flag and id_user[7] not in number[3:5]:
		return False
	elif flag == 0 and id_user[7] not in number[1:3]:
		return False

	# 함수 빠져나가기 전에 년도 앞 두 글자 19 또는 20을 미리 출력함
	if flag == 1:
		print('20', end='')
	else:
		print('19', end='')

	return True

def check_id(id_user):
	sex = ['남자', '여자', '남자', '여자']
	if not check_id_format(id_user) or not check_sex_index(id_user):
		print('Wrong id numbers. An id number format is ######-#######')
		print('Or just wrong number','Check the number and Try again',sep='\n')
		return
	
	print(f'{id_user[:2]}년 {id_user[2:4]}월 {sex[int(id_user[7]) - 1]}입니다')

#user_input = '500629-2222222'
#user_input = '010629-2222222'
user_input = '110629-3222222'
#user_input = '110629-1222222'

check_id(user_input)
