import string

file = input('Enter file :')

if len(file) < 1:
	file = 'clown.txt'

di = dict()
fh = open(file)
for line in fh:
	line = line.lower()
	line = line.translate(line.maketrans('', '', string.punctuation))
	words = line.split()
	for w in words:
		di[w] =  di.get(w, 0) + 1

# print(di)

lis = list()
for k, v in di.items():
	new_tuple = (v, k)
	lis.append(new_tuple)

sorted_tuple = sorted(lis, reverse=True)

for v, k in sorted_tuple[:5]:
	print(k, v)
