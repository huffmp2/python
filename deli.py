sandwiches = ['pastrami', 'tuna', 'roast beef', 'pastrami', 'grilled cheese']
finished = []
print ("The deli has run out of pastrami. ")
while 'pastrami' in sandwiches:
    sandwiches.remove('pastrami')
while sandwiches:
    current = sandwiches.pop()
    print ("Making your " + current.title() + " sandwich now!")
    finished.append(current)
print ("\nThe following sandwiches are ready:")
for finish in finished:
    print(finish.title())