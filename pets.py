pets= {
    'tina': {
        'breed': 'maltese',
        'color': 'white',
        'gender': 'female',
        'owner': 'greg',
        },
    'pepper':{
        'breed': 'poodle',
        'color': 'black and white',
        'gender': 'male',
        'owner': 'everett and dorothy',
        },
    'molly':{
        'breed': 'yellow labrador',
        'color': 'yellow',
        'gender': 'female',
        'owner': 'greg',
        },
    'holly':{
        'breed': 'black labrador',
        'color': 'black',
        'gender': 'female',
        'owner': 'greg',
        },
    }
for dog, info in pets.items():
    breed = info['breed']
    color = info['color']
    gender = info['gender']
    owner = info['owner']
    print ("A dog I used to know was named " + dog.title() + ". It was a " + gender + " " + breed.title() + ", had " + color + " fur, and was owned by " + 
    owner.title() + ".")