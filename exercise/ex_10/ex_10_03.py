fname = input('Enter file: ')
if len(fname) < 1:
	fname = 'mbox-short.txt'

di = dict()
fh = open(fname)
for line in fh:
	line = line.lower()
	print(line)
	for i in line:
		if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
			di[i] = di.get(i, 0) + 1
fh.close()

for key, val in sorted(di.items()):
	print(key, val)
