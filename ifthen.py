car = 'impala'
print ("Is car == 'impala'? I predict true")
print (car == 'impala')
dirt = '85'
print ("Are my grandparents older than 'dirt'? I predict two are, and one is not.")
evage= '88'
nanage= '86'
dorage= '84'
if 88 >= 85:
    print ("Grandpa Everett is older than dirt!")
if nanage >= dirt:
    print ("Grandma Nancy is older than dirt!")
if dorage >= dirt:
    print ("Grandma Dorothy is older than dirt!")
else:
    print ("Grandma Dorothy is not older than dirt!")
print ("Are all my grandparents older than dirt? I predict that is false.")
print (evage >= dirt and nanage >= dirt and dorage >= dirt)
print ("Are any of my grandparents younger than dirt?")
print (evage >= dirt or nanage >= dirt or dorage >= dirt)
print ("Which one?")
if dorage <= dirt:
    print ("Grandma Dorothy is not older than dirt!")
password = 'CatsGoneWild!'
print ("Is my password case sensitive? I predict it is.")
print (password == 'catsgonewild!')
print ("Now my password is not case sensitive.")
print (password.lower() == 'catsgonewild!')
meaning= '42'
print ("What is the meaning of life? I predict it is 42")
print (meaning == '42')
favauthor = ('Wen Spencer', 'Lois McMaster Bujold', 'John Scalzi', 'Patricia Briggs')
print ("Is one of my favorite authors Wen Spencer? I predict this is true.")
author= 'wen spencer'
if author.title() in favauthor:
    print ("One of my favorite authors is " + author.title() + ".")
else:
    print ("One of my favorite authors is not " + author.title() + ".")
print ("Is one of my favorite authors Jodi Piccoult? I predict this is not true.")
author= 'jodi piccoult'
if author.title() not in favauthor:
    print ("One of my favorite authors is not " + author.title() + ".")
else:
    print ("One of my favorite authors is " + author.title() + ".")
grands = 3
print ("Do I have four living grandparents? I think this is false")
if grands != 4:
    print ("I do not have four living grandparents.")