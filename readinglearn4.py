filename= 'learning_python.txt'

with open(filename) as file_object:
	lines= file_object.readlines()
	
pi_string= ' '
for line in lines:
	pi_string += line.replace('Python', 'C')
	
print(pi_string)