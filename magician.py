def magicians(names):
    """Print a list of magicians."""
    for magic in names:
        print (magic)

def makegreat(names):
    """Adding 'The Great' to the magician's names."""
    greatmagicians=[]
    while names:
        name=names.pop()
        greatmagician= name.title() + ' the Great'
        greatmagicians.append(greatmagician)
        print (greatmagicians)


names= ['david copperfield', 'harry houdini', 'david blaine']

magicians(names[:])

makegreat(names)

