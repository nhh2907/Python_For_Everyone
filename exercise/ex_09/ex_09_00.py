import string

f_name = input('Enter file: ')

di = dict()
fh = open(f_name)
for line in fh:
	line = line.rstrip()

	line = line.lower()
	print('Original: ', line)

	line = line.translate(line.maketrans('', '', string.punctuation))
	print('After : ', line)

	line = line.split()
	for word in line:
		if word not in di:
			di[word] = 1
		else:
			di[word] += 1
	
print(di)
