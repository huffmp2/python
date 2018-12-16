class Users():
	"""A class for user entry."""
	def __init__(self, firstname, lastname):
		"""Initialize name attributes."""
		self.firstname = firstname
		self.lastname= lastname
		self.loginattempts= 0
	def user(self):
		"""Describe the user."""
		print("The user's name is " + self.firstname.title()+ " " + self.lastname.title() + ".")
	def greet(self):
		"""Greet the user."""
		print("Thank you for joining our website, " + self.firstname.title() + ".")

class Privelages():
	"""A class to define admin privelages."""
	def __init__(self, powers=[]):
		self.powers= powers
		
	def showprivelages(self):
		"""Provides the name and privelages of an admin."""
		print ("An administrator has the following abilities: ")
		for power in self.powers:
			print ("- " + power)	
	
class Admin(Users):
	"""Defines a special class of users."""
	def __init__(self, firstname, lastname):
		"""initialize attributes of parent and child class."""
		super().__init__(firstname, lastname)
		self.privelages= Privelages()
		


admin1= Admin('mary', 'adams')
admin1.privelages.powers= ['can add post', 'can delete post', 'can ban user']
admin1.privelages.showprivelages()