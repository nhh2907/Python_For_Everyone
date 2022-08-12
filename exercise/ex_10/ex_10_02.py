user_input = input('Enter file: ')

if len(user_input) < 1:
	user_input = 'mbox-short.txt'

di = dict()
fh = open(user_input)
for line in fh:
	if not line.startswith('From '):
		continue
	line = line.split()

	di[line[5][:2]] = di.get(line[5][:2], 0) + 1
fh.close()

for key, val in sorted(di.items()):
	print(key, val)
