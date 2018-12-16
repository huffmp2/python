def buildperson(firstname, lastname, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': firstname, 'last': lastname}
    if age:
        person['age'] = age
    return person
musician = buildperson('jimi', 'hendrix', age='27')
print (musician)