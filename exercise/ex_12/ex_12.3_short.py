import re

f_name = 'regex_sum_1599281.txt'

fh = open('regex_sum_1599281.txt')

a = [int(i) for i in re.findall('[0-9]+', fh.read())]

print(sum(a))
