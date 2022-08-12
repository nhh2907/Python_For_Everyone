while True:
	try:
		f_name = input('Enter file: ')
		if len(f_name) < 1:
			f_name = 'mbox-short.txt'
		fhand = open(f_name)
		break
	except FileNotFoundError:
		print('File name is incorrect', 'Try again', sep='\n')
		continue

di = dict()
for line in fhand:
	if not line.startswith('From '):
		continue
	word_list = line.split()
	word = word_list[1]
	di[word] = di.get(word, 0) + 1
fhand.close()

largest_word = None
largest_count = None
for key, value in di.items():
	if largest_word is None or value > largest_count:
		largest_word = key
		largest_count = value

print(largest_word, largest_count)
