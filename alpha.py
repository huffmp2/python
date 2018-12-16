alpha= ['a', 'c', 'b', 'd', 'f', 'e', 'g']
message = "The two vowels in this list are " + alpha[0] + " and " + alpha[5] + "."
print (message)
alpha[0]= 'v'
print (alpha)
alpha= ['a', 'c', 'b', 'd', 'f', 'e', 'g']
alpha.append('v')
print (alpha)
alpha.insert(2, 'j')
print (alpha)
del alpha[3]
print (alpha)
endpop= alpha.pop()
print (alpha)
message= "The letter that doesn't belong is " + endpop + " because it is at the end of the alphabet." 
print (message)
alpha= ['a', 'c', 'b', 'd', 'f', 'e', 'g']
alpha.sort()
print (alpha)
alpha.sort(reverse=True)
print (alpha)
alpha= ['a', 'c', 'b', 'd', 'f', 'e', 'g']
print ("Here is the original list: ")
print (alpha)
print ("\nHere is the sorted list: ")
print (sorted(alpha))
print ("Here is the original list again: ")
print (alpha)
alpha.reverse()
print (alpha)
alpha = ['bmw', 'audi', 'toyota', 'subaru']
len(alpha)
print (len(alpha))
alpha= ['a', 'c', 'b', 'd', 'f', 'e', 'g']
print ("The first three letters in my list are:")
for alph in alpha[:3]:
    print(alph.title())
print ("Three letters in the middle of my list are:")
for alph in alpha[2:5]:
    print(alph.title())
print ("The last three letters in my list are:")
for alph in alpha[-3:]:
    print(alph.title())