import sys

count = 0
total = 0

fname = input('Enter a file name: ')

try:
	fhandle = open(fname)
except:
	print('There is no such a file.\nTry again')
	sys.exit()

for line in fhandle:
	line = line.rstrip()
	if not line.startswith('X-DSPAM-Confidence:'):
		continue
	index = line.find(':')
	sliced_line = float(line[index+1:])
	total = total + sliced_line
	count += 1

print('Average spam confidence: %.16f' % (total/count))
