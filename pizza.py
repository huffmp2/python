pizzas= ['mushroom and olive', 'garden', 'hawaiian']
for pizza in pizzas:
    print ("I like " + pizza + " pizza.")
print ("I really like pizza!")

pizzas= ['mushroom and olive', 'garden', 'hawaiian']
pizzas.append('supreme')
friendpizzas= pizzas[:]
friendpizzas.append('pepperoni')
print ("My friend's favorite pizzas are: ")
print (friendpizzas)
print ("\nMy favorite pizzas are: ")
print (pizzas)