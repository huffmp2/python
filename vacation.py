responses= {}
polling_active= True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Where would you go on your dream vacation? ")
    responses[name]= response
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active= False
print ("\n--- Poll Results ---")
for name, response in responses.items():
    print(name.title() + "'s dream vacation location is " + response + ".")