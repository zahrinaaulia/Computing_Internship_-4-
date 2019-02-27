class Vehicle:
	def __init__(self,year,price):
		self.year=year
		self.price=price

class Car(Vehicle):
	wheel_count = None
	capacity = None
	def pay_tax(self):
		pajak = float(self.price*0.15)
		return pajak
	def park(self,hour):
		biaya = 4*hour*1250
		if (capacity>5):
			biaya=biaya+5000
			return biaya
		else:
			return biaya

class Motorbike(Vehicle):
	wheel_count = None
	capacity = None
	def pay_tax(self):
		pajak = float(self.price*0.1)
		return pajak
	def park(self,hour):
		biaya = 2*hour*1250
		if (capacity>5):
			biaya=biaya+5000
			return biaya
		else:
			return biaya

class Bicycle(Vehicle):
	wheel_count = None
	capacity = None
	def pay_tax(self):
		return 0
	def park(self,hour):
		biaya = 2*hour*1250
		if (capacity>5):
			biaya=biaya+5000
			return biaya
		else:
			return biaya