class Pets:
	pet_list=[]
	def __init__(self,x):
		self.pet_list.append(x)
	def is_hungry(self):
		panjang = len(self.pet_list)
		for i in range(panjang):
			if(pet_list[i][2]==True):
				return True
		return False
	def whos_hungry(self):
		panjang = len(self.pet_list)
		for i in range(panjang):
			if(self.pet_list[i][2]==True):
				print(self.pet_list[i][0]+", ")

class Animal:
	def __init__(self, name, age, hungry):
		self.name = name
		self.age = age
		self.hungry = hungry
	def eat(self,name):
		panjang = len(self.pet_list)
		for i in range(panjang):
			if(self.pet_list[i][0]==name):
				self.pet_list[i][2]=False
				break

class Cat(Animal):
	species = None
	def sound(self):
		print("Miaw")

class Dog(Animal):
	species = None
	def sound(self):
		print("Gukguk")

class Bird(Animal):
	species = None
	def sound(self):
		print("PritPrit")