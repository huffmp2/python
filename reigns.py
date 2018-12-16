favnumbers= {'dasher': ['3', '7'],
    'dancer': ['1', '8'], 
    'prancer': ['9', '10'],
    'vixen':['2','6'],
    'comet': ['5','15'],
    }
for name, numbers in favnumbers.items():
    print (name.title() + "'s favorite numbers are: ")
    for number in numbers:
        print("\t" + number.title())
