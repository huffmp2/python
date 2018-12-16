alien0= {'color': 'green', 'points': 5}
print (alien0['color'])
print (alien0['points'])

newpoints = alien0['points']
print ("You just earned " + str(newpoints) + " points!")

alien0['xposition']=0
alien0['yposition']=25
print (alien0)

print ("The alien is " + alien0['color'] + ".")
alien0['color']= 'yellow'
print ("The alien is now " + alien0['color'] + ".")

alien0 = {'xposition': 0, 'yposition': 25, 'speed': 'medium'}
print ("Original x-position: " + str(alien0['xposition']))
#Move the alien to the right.
#Determine how far to move the alien base on its current speed.
if alien0['speed'] == 'slow':
    xincrement=1
elif alien0['speed'] == 'medium':
    xincrement= 2
else:
    xincrement= 3
alien0['xposition'] = alien0['xposition'] + xincrement
print ("New x-position: " + str(alien0['xposition']))

alien0= {'color': 'green', 'points': 5}
del alien0['points']
print (alien0)