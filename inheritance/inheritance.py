class Parent():
	def __init__(self, last_name, eye_color):
		print("Parent Constructor called")
		self.last_name = last_name
		self.eye_color = eye_color
	
	def show_info(self):
		print("last name: " + self.last_name)
		print("Eye color: " + self.eye_color)

# To inherit Parent class in Child class, use the following notation
class Child(Parent):
	def __init__(self, last_name, eye_color, number_of_toys):
		print("Child Constructor called")
		Parent.__init__(self, last_name, eye_color)
		self.number_of_toys = number_of_toys

	def show_info(self):
		print("last name: " + self.last_name)
		print("Eye color: " + self.eye_color)
		print("Number of toys: " + str(self.number_of_toys)



	

# billy_cyrus = Parent("Cyrus", "blue")
# print(billy_cyrus.last_name)

miley_cyrus = Child("Cyrus", "Blue", 5)
print(miley_cyrus.last_name)
print(miley_cyrus.number_of_toys)
