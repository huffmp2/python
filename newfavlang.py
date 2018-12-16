from collections import OrderedDict

favlang = OrderedDict()

favlang['jen']= 'python'
favlang['sarah']= 'c'
favlang['edward']= 'ruby'
favlang['phil']= 'python'
	
for name, language in favlang.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
	

	