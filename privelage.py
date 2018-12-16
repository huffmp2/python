from user import Users

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