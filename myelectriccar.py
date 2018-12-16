from car import ElectricCar


mytesla= ElectricCar('tesla', 'model s', 2016)
print (mytesla.get_descriptive_name())

mytesla.battery.describebattery()
mytesla.battery.getrange()