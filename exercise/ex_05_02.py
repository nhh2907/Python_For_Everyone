# set None type to variables because we don't know what users input
smallest = None
largest = None

while True:
	# Request user's input and check if it is 'done' for finish
	answer = input("(Enter 'done' to finish) Enter a number: ")
	if answer == 'done':
		break

	# check if input is a numeric number
	try:
		int_answer = int(answer)
	except:
		print('Invalid input')
		continue

	# Sort Max and Min number
	if smallest is None or largest is None:
		smallest = int_answer
		largest = int_answer
		continue
	elif int_answer < smallest:
		smallest = int_answer
	elif int_answer > largest:
		largest = int_answer

print(f'Maximum is {largest}\nMinimum is {smallest}')  
