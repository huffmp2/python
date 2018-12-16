family= {
    'mother': {
        'firstname': 'diane', 
        'lastname': 'walker', 
        'age': '59', 
        'city': 'everett',
        },
    'father': { 
        'firstname': 'chuck', 
        'lastname': 'Huffman', 
        'age': '60', 
        'city': 'tule lake',
        },
    'brother': {
        'firstname': 'Greg', 
        'lastname': 'Huffman', 
        'age': '36', 
        'city': 'Boise',
        },
    }
    
for relative, info in family.items():
    fullname= info['firstname'] + " " + info['lastname']
    location = info['city']
    print("\nMy " + relative + "'s name is " + fullname.title() + ". They live in " + location.title() + ".")