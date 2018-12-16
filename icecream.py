class Restaurant():
	"""A simple attempt to model a restaurant."""
	def __init__(self, name, cuisine):
		"""Initialize name and age attributes."""
		self.name = name
		self.cuisine= cuisine
		self.numberserved= 0
	def what(self):
		"""Talk about the restaurant."""
		print(self.name.title() + " is a " + self.cuisine + " restaurant.")
	def open(self):
		"""Announce the restaurant is open."""
		print(self.name.title() + " is now open.")

class Icecream(Restaurant):
	"""Represent aspects of a restaurant, specific to and icecream stand."""
	def __init__(self, name, cuisinetype= 'ice cream'):
		"""Initialize attributes of the parent class. Then initialize attributes specific to an icecream stand."""
		super().__init__(name, cuisinetype)
		
		self.flavors= []
		self.name= name
		
	def listflavors(self):
		"""Provide customers a description of the ice cream flavors."""
		print ("My ice cream stand serves the following ice cream flavors.")
		for flavor in self.flavors:
			print ("- " + flavor.title())

		
mystand=Icecream('neopolitan rocks')

mystand.flavors= ['chocolate', 'vanilla', 'strawberry']

mystand.listflavors()
