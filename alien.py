alien = 'red'
if alien == 'green':
    print ("Killed Green Alien! 5 points!")

alien = 'red'
if alien == 'red':
    print ("Killed Red Alien! 5 points!")
alien = 'red'
if alien == 'green':
    print ("Shot Green Alien! 5 points!")
if alien != 'green':
    print ("10 points!")

if alien == 'green':
    print ("Shot Green Alien! 5 points!")
else:
    print ("10 points!")
alien = 'green'
if alien == 'green':
    print ("Shot Green Alien! 5 points!")
elif alien != 'yellow':
    print ("Shot Yellow Alien! 10 points!")
else:
    print ("Shot Red Alien! 15 points!")
alien = 'yellow'
if alien == 'green':
    print ("Shot Green Alien! 5 points!")
elif alien != 'yellow':
    print ("Shot Yellow Alien! 10 points!")
else:
    print ("Shot Red Alien! 15 points!")
alien = 'red'
if alien == 'green':
    print ("Shot Green Alien! 5 points!")
elif alien != 'yellow':
    print ("Shot Yellow Alien! 10 points!")
else:
    print ("Shot Red Alien! 15 points!")