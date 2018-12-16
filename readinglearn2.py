filename= 'learning_python.txt'

with open(filename) as file_object:
	for line in file_object:
		message= line.rstrip()
		message.replace('Python', 'C')
		print(message)
		