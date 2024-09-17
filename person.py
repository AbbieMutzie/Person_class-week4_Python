class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello! My name is {self.name}. I am {self.age} years old, and I identify as a {self.gender}")

#Creating an instance of the Person
person1 = Person("Abigael", 24, "Female")

#Calling the introduce method
person1.introduce()
