prompt= input("How old are you?")
prompt = int(prompt)

if prompt <= 3:
    print ("Your ticket is free!")
elif prompt <= 12:
    print ("Your ticket is $10!")
else:
    print ("Your ticket is $15!")
while prompt < 12:
    prompt= input ("Children must be accompanied by an adult. Please enter your age.")
    prompt = int(prompt)
    if prompt <= 3:
        print ("Your ticket is free!")
    elif prompt <= 12:
        print ("Your ticket is $10!")
    else:
        print ("Your ticket is $15!")
    
