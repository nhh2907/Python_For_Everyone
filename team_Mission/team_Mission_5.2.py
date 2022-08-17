def grader(names_and_scores, correct_answers):
	count = 0
	lis = list()

	for person in names_and_scores:
		person = person.split(',')
		count = 0
		for i in range(len(correct_answers)):
			if int(person[1][i]) == correct_answers[i]:
				count += 1
			i += 1
		new_tuple = (count * 10, person[0]) # 맞은 개수 곱하기 10 = 점수
		lis.append(new_tuple)

	lis.sort(reverse=True)

	i = 0
	for score, name in lis:
		i += 1
		print(f"학생: {name}, 점수: {score}, {i}등")

names_and_scores = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]
correct_answers = [3,2,4,2,5,2,4,3,1,2]

grader(names_and_scores, correct_answers)
