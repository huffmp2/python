def magicians(names):
    """Print a list of magicians."""
    for name in names:
        msg= name.title() + " is a famous magician!"
        print(msg)
names= ['david copperfield', 'harry houdini', 'david blaine']
magicians(names)