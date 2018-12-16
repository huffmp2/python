favlang= {'jen': 'python',
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python',
    }
print ("Sarah's favorite language is " + 
    favlang['sarah'].title() + ".")
    
for name, language in favlang.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
    
for name in favlang.keys():
    print(name.title())
    
friends= ['phil', 'sarah']
for name in favlang.keys():
    print(name.title())
    if name in friends:
        print (" Hi " + name.title() + ", I see your favorit languague is " + favlang[name].title() + "!")

if 'erin' not in favlang.keys():
    print("Erin, please take our poll!")
    
for name in sorted(favlang.keys()):
    print (name.title() + ", thank you for taking the poll.")
    
print ("The following languages have been mentioned:")
for language in favlang.values():
    print(language.title())
    
for language in set(favlang.values()):
    print(language.title())