class Car():
	"""A simple attempt to represent a car."""
	
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make= make
		self.model= model
		self.year= year
		self.odometer= 25
	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name= str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
	def readodometer(self):
		"""Print a statement showing the car's mileage."""
		print("This car has " + str(self.odometer) + " miles on it.")
	def updateodometer(self, mileage):
		"""Set the odometer reading to the given value. Reject the change if it attempts to roll the odometer back."""
		if mileage >= self.odometer:
			self.odometer= mileage
		else:
			print("You can't roll back an odometer!")
		
	def incrementodometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometer += miles
		
mynewcar = Car('audi', 'a4', 2016)
print (mynewcar.get_descriptive_name())

mynewcar.updateodometer(23)
mynewcar.readodometer()

myusedcar= Car('subaru', 'outback', 2013)
print (myusedcar.get_descriptive_name())

myusedcar.updateodometer(23500)
myusedcar.readodometer()

myusedcar.incrementodometer(100)
myusedcar.readodometer()