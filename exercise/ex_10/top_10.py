# 가장 많이 등장한 단어 Top 10 출력하기

import string

dic = dict()
fh = open('romeo.txt')
for line in fh:
	line = line.translate(line.maketrans('','',string.punctuation))
	words = line.split()
	for word in words:	
		dic[word] = dic.get(word, 0) + 1
fh.close()
#print(dic)

# value로 정렬하기 위해 key와 value를 서로 바꿈
lis = list()
for k, v in dic.items():
	lis.append((v, k))
#print(lis)

# Tuple끼리 비교 가능함. 첫번째 원소끼리 비교하고 같지 않은 경우에만
# 두번째 원소끼리 비교함
lis_sorted = sorted(lis, reverse=True)

# key와 value를 변경했던 것을 다시 서로 바꾸고 출력
for v, k in lis_sorted[:10]:
	print(k, v)
