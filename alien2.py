alien0= {'color': 'green', 'points': '5'}
alien1= {'color': 'yellow', 'points': '10'}
alien2= {'color': 'red', 'points': '15'}
aliens = [alien0, alien1, alien2]

for alien in aliens:
    print(alien)
 
# Make an empty list for storing aliens.
 
aliens = []

# Make 30 green aliens.

for aliennumber in range(30):
    newalien= {'color':'green', 'points': '5', 'speed': 'slow'}
    aliens.append(newalien)

# Show the first 5 aliens.

for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.

print("Total number of aliens: " + str(len(aliens)))


# Make an empty list for storing aliens.
 
aliens = []

# Make 30 green aliens.

for aliennumber in range(30):
    newalien= {'color':'green', 'points': '5', 'speed': 'slow'}
    aliens.append(newalien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'
        
# Show the first 5 aliens.

for alien in aliens[:5]:
    print(alien)
print("...")
