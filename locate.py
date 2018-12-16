def cities(name, country = 'canada'):
    """Describes the name and location of a city."""
    print ("The city of " + name.title() + " is located in " + country.title() + ".")
cities ('montreal')
cities ('quebec')
cities ('new york', country='USA')