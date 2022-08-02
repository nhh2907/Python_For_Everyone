# 다음 코드는 if문 없이 이진 탐색 bisect로 구현함
def perform_grader(score, name):
	import bisect

	table = [60, 65, 70, 75, 80, 85, 90, 95]
	grade = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A', 'A+']

	index = bisect.bisect_right(table, score)

	print(f'Your name : {name}')
	print(f'Your score : {score}')
	print(f'Your grade : {grade[index]}')

score_user = int(input('What is your score? '))
name_user = input('What is your name? ')
perform_grader(score_user, name_user)
