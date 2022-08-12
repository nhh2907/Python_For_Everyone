def split_file(file_name):
	result = list()
	file_handle = open(file_name)
	for line in file_handle:
		line = line.split()
		for word in line:
			if word in result:
				continue
			result.append(word)
	result.sort()
	print('All the words: ', result)

input_user = input('Enter the file name ')
split_file(input_user)
