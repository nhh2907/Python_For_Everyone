# Python Doc 3.10.5 - Ch.6 Module Description

def fibo(n):
	""" Write Fibonacci series up to n """

	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
	print()

def fibo_list(n):
	""" Return Fibonacci series up to n """

	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a+b
	return result

if __name__ == "__main__":
	import sys
	fibo(int(sys.argv[1]))

