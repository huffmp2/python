print("Give me two numbers, and I'll add them.")
first_number = input("\First number: ")
second_number = input("Second number: ")
try: 
	answer = int(first_number) + int(second_number)
except ValueError:
	print("Please use digits only.")
else:
	print(answer)