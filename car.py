class Car():
	"""A simple attempt to represent a car."""
	
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make= make
		self.model= model
		self.year= year
		self.odometer= 0
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
		
class Battery():
	"""A simple attempt to model a batter for an electric car."""
	def __init__(self, batterysize=70):
		"""initialize the battery's attributes."""
		self.batterysize= batterysize
	def describebattery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.batterysize) + "-kWh battery.")
	def getrange(self):
		"""Print a statement about the range this battery provides."""
		if self.batterysize == 70:
			range = 240
		elif self.batterysize == 85:
			range = 270
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)
	
	def upgradebattery(self, bettersize):
		"""Makes sure the battery is the best possible."""
		self.batterysize= bettersize
		
class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class. Then initialize attributes specific to an electric car."""
		super().__init__(make, model, year,)
		self.battery= Battery()