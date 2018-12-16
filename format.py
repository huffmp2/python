def formatname(firstname, lastname, middlename= ''):
    """Return a full name neatly formatted."""
    if middlename:
        fullname= firstname + ' ' + middlename + ' ' + lastname
    else:
        fullname= firstname + ' ' + lastname
    return fullname.title()
while True:
    print("\nPlease tell me your name: ")
    print ("(enter 'q' at any time to quit)")
    fname = input("First Name: ")
    if fname == 'q':
        break
    lname= input("Last Name: ")
    if lname == 'q':
        break
    formattedname= formatname(fname, lname)
    print("\nHello, " + formattedname + "!")