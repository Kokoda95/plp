# Create Person class.
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        print(f'Hello! my name is {self.name}. I am {self.age} year old and my gender is {self.gender}.')    
# Create the instance of the class.
p1 = Person("Kokoda", 28, "male")
# Call the introduce method on the object. 
p1.introduce()