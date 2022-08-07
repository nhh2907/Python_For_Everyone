def count_word(sentence, find_word):
	
	fh = open('Q4.2.txt', 'w')
	fh.write(sentence)
	fh.close()
	
	count = sentence.count(find_word)
	print(f'The word count:  "{count}"')

user_input = input('''Enter a sentence: ''')
word = input('Enter a word to find: ')

count_word(user_input, word)
