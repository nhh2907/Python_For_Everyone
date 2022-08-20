def manage_members(names, records):
	di = dict()
	new_list = list()

	# 평균을 구하고 딕셔너리에 삽입
	i = 0
	for name in names:
		avg= sum(records[i]) / len(records[i])
		di[name] = avg
		i += 1	

	# (평균값, 이름) 튜플로 새로운 리스트에 삽입
	for name, avg in di.items():
		new_list.append((avg, name))

	# 내림차순으로 정렬
	new_list.sort(reverse=True)

	for avg, name in new_list:
		if avg > 5 and (avg, name) in new_list[:2]:
			print(f"보너스 대상자 {name}")
		if avg <= 3 and (avg, name) in new_list[-2:]:
			print(f"면담 대상자 {name}")


		
member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
member_records = [[4,5,3,5,6,5,3,4,1,3,4,5],[2,3,4,3,1,2,0,3,2,5,7,2],
           [1,3,0,3,3,4,5,6,7,2,2,1],[3,2,9,2,3,5,6,6,4,6,9,9],
           [8,7,7,5,6,7,5,8,8,6,10,9],[7,8,4,9,5,10,3,3,2,2,1,3]]

manage_members(member_names, member_records)
