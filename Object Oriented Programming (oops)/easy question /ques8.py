class Animal:
    pass

class Dog(Animal):
    pass

# Creating some objects
a = Animal()
d = Dog()
name = "Buddy"
age = 5

# Let's check their types using isinstance()
print(isinstance(a, Animal))  
print(isinstance(d, Dog))     
print(isinstance(d, Animal))  
print(isinstance(name, str))  
print(isinstance(age, int))   
print(isinstance(age, float)) 
