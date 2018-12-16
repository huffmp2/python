def count_word(filename):
	"""Count the number of times a word appears in a text."""
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		msg= "Sorry, the file " + filename + " does not exist."
		print (msg)
	else:
		"""Count the number of times a specific word is used in the file."""
		words = contents.lower().split()
		words = words.count('the')
		print ("The file " + filename + " used the word 'the' " + str(words) + " times.")
		
filenames= ['pride_and_prejudice.txt', 'dracula.txt']
for filename in filenames:
	count_word(filename)