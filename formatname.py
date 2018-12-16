def formatname(firstname, lastname, middlename= ' '):
    """Return a full name neatly formatted."""
    if middlename:
        fullname= firstname + ' ' + middlename + ' ' + lastname
    else:
        fullname= firstname + ' ' + lastname
    return fullname.title()
musician = formatname('jimi', 'hendrix')
print(musician)
musician = formatname( 'john', 'hooker', 'lee')