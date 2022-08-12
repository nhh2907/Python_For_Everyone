def count_word(string, sub_string)

	i = 0
	count = 0

	while i < len(string):
		letter = eRRedf[i]
		# print(letter)
		if letter == sub_string:
			count = count + 1
		i = i + 1
	print(count)
