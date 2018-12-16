guests= ['Abe', 'George', 'Frank']
print (guests)
message = "Hello " + guests[0] + ", please come to my dinner party."
print (message)
message = "Hello " + guests[1] + ", please come to my dinner party."
print (message)
message = "Hello " + guests[2] + ", please come to my dinner party."
print (message)
guests= ['Abe', 'George', 'Frank']
message = "Hi " + guests[0] + ", sorry you couldn't make it! I hope the headache clears up soon."
print (message)
del guests[0]
guests.insert(0, 'Thomas')
print (guests)
message = "Hi " + guests[0] + ", " + guests[1] + ", "+ guests[2] + ",  you will be happy to know I found a larger table. Your wives or hostesses, will be sent an invitation."
print (message)
guests.insert (2,'Martha')
guests.append('Eleanor')
guests.insert(0, 'Dolly')
print (guests)
message = "Hello " + guests[0] + ", please come to my dinner party."
print (message)
message = "Hello " + guests[3] + ", please come to my dinner party."
print (message)
message = "Hello " + guests[5] + ", please come to my dinner party."
print (message)
message = "Hello, I apologize but the large table with not arrive in time."
print (message)
guests = ['Dolly', 'Thomas', 'George', 'Martha', 'Frank', 'Eleanor']
ung1= guests.pop()
message = "Hi " + ung1 + ", I am sorry, but I must rescind my invitation."
print (message)
ung2= guests.pop()
message = "Hi " + ung2 + ", I am sorry, but I must rescind my invitation."
print (message)
ung3= guests.pop()
message = "Hi " + ung3 + ", I am sorry, but I must rescind my invitation."
print (message)
ung4= guests.pop()
message = "Hi " + ung4 + ", I am sorry, but I must rescind my invitation."
print (message)
print (guests)
del guests[0]
del guests[0]
print (guests)

