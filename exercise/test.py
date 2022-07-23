name = 'apple' 
index = 0
count = 0
while index < len(name):
	letter = name[index]
	# print(letter)
	if letter == 'p':
		count = count + 1
	index = index + 1
print(count)

