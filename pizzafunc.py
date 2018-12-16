def makepizza(size, *toppings):
    """Print the list of toppings that have been requestd."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)
