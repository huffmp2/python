polled= {'jen': 'python',
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python',
    }

shbpolled= ['jen', 'peter', 'phil', 'andrew']


for name in polled.keys():
    print ("Hi " + name.title() + ", thank you for taking our poll!")

for shb in shbpolled:
    if shb not in polled:
        print ("Hi " + shb.title() + ", please take our poll!")