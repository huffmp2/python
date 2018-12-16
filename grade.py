responses= {}
polling_active= True
while polling_active:
    names = input("\nWhat is your name? ")
    grade = input("\nWhat is your grade? ")
    grade = int(grade)
    responses[names]= grade
    repeat = input("Would you like to add another grade? (yes/ no) ")
    if repeat == 'no':
        polling_active= False
print ("\n--- Grades ---")
for names, grade in responses.items():
	if grade >= 89:
		print (names.title() + "'s grade is an A.")
	elif grade >= 79:
		print (names.title() + "'s grade is a B.")
	elif grade >= 69:
		print (names.title() + "'s grade is a C.")
	elif grade >= 59:
		print (names.title() + "'s grade is a D.")
	else:
		print (names.title() + "'s grade is N/C.")
