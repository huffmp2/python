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
	def customers(self):
		"""Detail the number served."""
		print("This restaurant has served " + str(self.numberserved) + " customers.")
	def updatenumberserved(self, people):
		"""Update the number of customers served."""
		self.numberserved= people
	def incrementnumberserved(self, newpeople):
		"""Add new customers."""
		self.numberserved+= newpeople

my_restaurant = Restaurant('silver dragon', 'chinese')		
print ("My restaurant's name is " + my_restaurant.name.title() + ". It serves fine " + my_restaurant.cuisine + " food.")

my_restaurant.what()
my_restaurant.open()

print ("My restaurant has served " + str(my_restaurant.numberserved) + " people.")

my_restaurant.updatenumberserved(56)
my_restaurant.customers()

my_restaurant.incrementnumberserved(20)
my_restaurant.customers()