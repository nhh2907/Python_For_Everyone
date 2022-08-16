def grader(s, a):
	count = 0
	lis = list()

	for person in s:
		person = person.split(',')
		count = 0
		for i in range(len(a)):
			if int(person[1][i]) == int(a[i]):  # 왜 int형변환 해야만 작동하는지 모르겠어요
				count += 1
			i += 1
		new_tuple = (count*10, person[0]) # 맞은 개수 곱하기 10 = 점수
		lis.append(new_tuple)

	lis.sort(reverse=True)

	i = 0
	for score, name in lis:
		i += 1
		print(f"학생: {name}, 점수: {score}, {i}등")

s = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]
a = [3,2,4,2,5,2,4,3,1,2]

grader(s, a)
