favplaces= {
    'greg': ['golf course', 'john deere store'],
    'pam': ['book store', 'library'],
    'diane': ['park', 'antique store', 'church'],
    }
for name, places in favplaces.items():
    for place in places:
        print (name.title() + "'s favorite places include a " + place + ".")