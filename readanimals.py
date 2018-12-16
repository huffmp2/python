def read_words(filename):
	"""Print the words in a file."""
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		pass
	else:
		"""Print the words in the file."""
		print(contents)
		
filenames= ['cats.txt', 'dogs.txt']
for filename in filenames:
	read_words(filename)