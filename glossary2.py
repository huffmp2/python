from collections import OrderedDict

glossary= OrderedDict()

glossary['if-elif-else']= 'a way to determine if input matches one of multiple set conditions, and what to do if it does not'
glossary['float']= 'A number with a decimal point'
glossary['string']= 'a series of characters'
glossary['traceback']= 'a record of where the interpreter could not read code'
glossary['variable']= 'code that holds or points to a value'
glossary['value']= 'the entry that is either printed on the screen or otherwise defines a variable'
glossary['loop']= 'a program that tests each item in a list, dictionary or other container'
glossary['tupple']= 'a list that cannot be changed'
glossary['list']= 'a collection of items grouped together using brackets'
glossary['key']= 'the first part of a key value set that defines the value'

for terms, definitions in glossary.items():
    print (terms.title() + " is defined as: " + definitions + ".")