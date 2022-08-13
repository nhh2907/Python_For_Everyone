def do_times_table(number):
	print(f"{number} times table")
	result = [f"{number} x {i}" for i in range(1, 10, 2) if i*number <= 50]	
	print(*result, sep='\n')  # "*" means unpack

number = int(input('Enter the number of times: '))

do_times_table(number)
