reqtoppings= ['mushrooms', 'green peppers', 'extra cheese']
for reqtopping in reqtoppings:
    if reqtopping == 'green peppers':
        print ("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + reqtopping + ".")
print ("Finished making your pizza!")
reqtoppings= []
if reqtoppings:
    for reqtopping in reqtoppings:
        print ("Adding " + reqtopping + ".")
    print ("\nFinished making your pizza!")
else:
    print ("Are you sure you want a plain pizza?")
availtop= ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
reqtoppings = ['mushrooms', 'french fries', 'extra cheese']
for reqtopping in reqtoppings:
    if reqtopping in availtop:
        print ("Adding " + reqtopping + ".")
    else:
        print ("Sorry, we don't have " + reqtopping + ".")
print ("\nFinished making your pizza!")