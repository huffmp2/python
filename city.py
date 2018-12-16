prompt= "\nPlease enter the name of a city you have visited:"
    prompt += "\nenter 'quit' when you are finished.) "
while True:
    city= input(prompt)
if city == 'quit':
    break
else:
    print ("I'd love to to " + city.title() + "!")