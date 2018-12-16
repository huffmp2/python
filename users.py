class Users():
	"""A clase for user entry."""
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
	def readattempts(self):
		"""Print a statement showing number of login attempts."""
		print("You have tried to log in  " + str(self.loginattempts) + " times.")
	def updateattempts(self, attempts):
		"""Updates the number of login attempts."""
		self.loginattempts= attempts
	def incrementloginattempts(self):
		"""Increases the number of login attempts."""
		self.loginattempts+= 1
	def resetloginattempts(self):
		"""Rest the number of login attempts."""
		self.loginattempts= 0
		
user1= Users('pam', 'huffman')	

user1.user()
user1.greet()
user1.updateattempts(1)
user1.readattempts()

user1.incrementloginattempts()
user1.readattempts()

user1.resetloginattempts()
user1.readattempts()
