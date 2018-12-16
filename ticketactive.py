age= input("How old are you? ")
age= int(age)
active = True
while active: message = input(age)
message = int(age)
if message >= 12:
    active= False
else:
    message= input("Children must be accompanied by an adult. Please enter your age.")
    message = int(age)
