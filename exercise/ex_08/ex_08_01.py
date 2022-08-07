def middle(list_):
	print(list_)
	print(list_ is test)
	print(list_[:] is test)  # false. 왜냐하면 슬라이싱 오퍼레이터는 새로운 리스트 객체를 만들어내기 때문
	print(list_[:])
	print(id(list_[:]))
	print(id(test))
	list_ = list_[1:len(list_)-1]
	print(list_ is test)
	return list_

def chop(list_):
	
	# del statement, not del function
	# del statement do not return a removed value,
	# while pop function return a removed value
	del list_[0]
	del list_[len(list_) - 1]

	return list_

test = [1, 2, 3, 4, 5]
print('Original list', test, '\n')
print('New slice-created list in function', middle(test))
print('Original list', test, '\n')
print(chop(test))

