from random import randint

class Die():
	"""A simple dice model."""
	def __init__(self, side=6):
		
		"""Initialize side attribute."""
		self.side = side
	
	def rolldie(self):
		"""Roll a die."""
		return randint(1, self.side)
	
	def updatedie(self, newside):
		"""Update the number of sides of a die."""
		self.side=newside
		
mydie= Die()
results= []
for rollnum in range(10):
	result= mydie.rolldie()
	results.append(result)
print("10 rolls of a 6 sided die:")
print(results)

my2nddie= Die()
my2nddie.updatedie(10)
results= []
for rollnum in range(10):
	result= my2nddie.rolldie()
	results.append(result)
print("10 rolls of a 10 sided die:")
print(results)

my3rddie= Die()
my3rddie.updatedie(20)
results= []
for rollnum in range(10):
	result= my3rddie.rolldie()
	results.append(result)
print("10 rolls of a 20 sided die:")
print(results)