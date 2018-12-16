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
