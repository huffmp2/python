def printmodels(unprinted, completed):
    """Simulate printing each design, until none are left. 
    Move each design to completedmodels after printing."""
    while unprinted:
        current= unprinted.pop()
        print("Printing model: " + current)
        completed.append(current)
def showcompleted(completed):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for complete in completed:
        print(complete)

