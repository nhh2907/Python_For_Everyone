fhandle = open('mbox-short.txt')

for line in fhandle:
	line = line.rstrip()
	if not line.startswith('To:'):
		continue
	line = line.upper()
	print(line)
