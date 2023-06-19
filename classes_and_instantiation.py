# Classes

# Creating a class - this is like a template
class Dog:
    animal_kind ="canine" # class variable


    def bark(self): # class functions = methods
        self.animal_kind

        return "woof"

# print(Dog.animal_kind)
# print(Dog.bark(Dog))

# Instantiation

fido = Dog()
lassie = Dog()

print(type(fido)) # <class '__main__.Dog'>
print(type(lassie)) # <class '__main__.Dog'>
print(lassie.animal_kind) # canine
print(fido.bark()) # woof

# Class variables can be overwritten

fido.animal_kind = "Big Dog"
print(lassie.animal_kind) # canine
print(fido.animal_kind) # big dog

# Be careful of class variables

Dog.animal_kind = "Dolphin"
print(lassie.animal_kind) # dolphin
print(fido.animal_kind) # big dog

print(fido.bark()) # woof













