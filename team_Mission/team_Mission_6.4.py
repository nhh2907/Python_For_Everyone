def is_vip(info):
	# 여러 개의 category이므로 categories 복수형 사용
	categories = ['아이디', '나이', '전화번호', '성별', '지역', '구매횟수']
	info = info.split(',')
	
	# 모든 원소를 확인하고 categories를 key로 하여 딕셔너리에 value로 삽입
	di = dict()
	n = len(info)
	i = 0
	for _ in info[:6]:
		count = 0
		for _ in range(n - i):  # range(n)으로해도 결과는 같지만 연산 줄이기 위해 i를 뺌
			if count % 6 == 0:
				di[categories[i]] = di.get(categories[i], list()) + [info[count + i]] 
			count += 1
		i += 1
	
	# 전화번호 없는 부분만 '000-0000-0000'로 딕셔너리 업데이트
	i = 0
	for tel_num in di['전화번호']:
		if tel_num == 'x':
			di['전화번호'][i] = '000-0000-0000'
		i += 1
	
	# 질문: 모든 변수를 딕셔너리 익덱스로 모든 것을 표현했는데 혹시 더 간단한 방법이 있나요?
	for i, num in enumerate(di['구매횟수']):
		if int(num) >= 8 and di['전화번호'][i] != '000-0000-0000':
			print(
			f"할인 쿠폰을 받을 회원정보 아이디:{di['아이디'][i]},\
			나이:{di['나이'][i]}, \
			전화번호:{di['전화번호'][i]}, \
			성별:{di['성별'][i]}, \
			지역:{di['지역'][i]}, \
			구매횟수: {num}"
			)

info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"

is_vip(info)
