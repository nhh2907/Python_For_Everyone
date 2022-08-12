def extract_email(file):
	count = 0
	f_handle = open(file)
	for i in f_handle:
		word = i.split()
		if len(word) == 0 or word[0] != 'From' :  # Guard Evaluation
			continue
		count += 1
		print(word[1])
	print(f'There were {count} lines in the file with From as the first word')

user_input = input('Enter a file name ')
extract_email(user_input)
