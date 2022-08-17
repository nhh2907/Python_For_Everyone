import re

f_name = 'regex_sum_1599281.txt'

sum_re = 0
count = 0
fh = open(f_name)
for line in fh:
	line = line.rstrip()
	list_number = re.findall('[0-9]*', line)
	print(list_number)
	if len(list_number) < 1:
		continue
	count = count + len(list_number)
	print(list_number)
	for i in list_number:
		sum_re = sum_re + int(i)
fh.close()

#print(sum_re)
#print(count)
