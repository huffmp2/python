def makesandwich(*fillings):
    """Print the list of sandwhich fillings that have been requestd."""
    print("\nMaking a sandwich with the following fillings: ")
    for filling in fillings:
        print("- " + filling)
