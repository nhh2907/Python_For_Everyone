count = {}
file = open('clown.txt', 'r')
for line in file:
	line = line.split()
	for word in line:
		count[word] = count.get(word, 0) + 1
file.close()

big_word = None
big_count = None
for key, val in count.items():
	if big_word == None or val > big_count:
		big_word = key
		big_count = val

print(big_word, big_count)
