usernames= []
if usernames:
    for user in usernames:
        print (" Hello " + user.title() + ", thank you for logging in again.")
else:
    print ("We need to find users!")

currentusers= ['Tom', 'Dick', 'Harry', 'Ronald', 'Dudley']
newusers= ['harry', 'Peter', 'Ducky', 'RONALD']
for newuser in newusers:
    if newuser.title() in currentusers:
        print ("\nI'm sorry, the username " + newuser.title() + " is not 
        available. Please enter a new one.")
    else:
        print ("The username " + newuser.title() + " is available.")
        
