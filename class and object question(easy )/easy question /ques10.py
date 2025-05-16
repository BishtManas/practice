class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"My name is {self.name} and I am {self.age} years old."

# Creating an object of the Person class
p1 = Person("Manav", 21)

# Printing the object — this will call __str__() automatically
print(p1)
