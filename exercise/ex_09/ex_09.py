f_name = input('Enter file: ')
if len(f_name) < 1:
	f_name = 'intro.txt'

dict_file = dict()
fhand = open(f_name)
for line in fhand:
	line = line.rstrip()
	words = line.split()
	for word in words:
		dict_file[word] = dict_file.get(word, 0) + 1
fhand.close()

# print(dict_file)

largest_word = None
largest_count = None
for key, value in dict_file.items():
	if largest_word is None or value > largest_count:
		largest_word = key
		largest_count = value

print('The largest word: %s\nThe largest count: %s'\
	% (largest_word, largest_count))
