# # code ada bbrp jenis
# # the usual one is procedural
# # we are going to learn about oop

# OOP (Object-Oriented Programming) is a programming paradigm that organizes code into objects—bundles 
# of data and behavior—so systems are easier to design, extend, and maintain.

# Core ideas (4 pillars):
# Encapsulation – Keep data and methods together; hide internal details and expose only what’s needed.
# Abstraction – Show what an object does, not how it does it (e.g., interfaces/abstract classes).
# Inheritance – Create new classes from existing ones to reuse and extend behavior.
# Polymorphism – Different objects can respond to the same method call in different ways.

# Base class (Abstraction + Encapsulation)
# class Animal:
#     def __init__(self, name):
#         self.name = name  # encapsulated data

#     def speak(self):
#         raise NotImplementedError("Subclasses must implement this method")


# # Child class (Inheritance)
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says Woof!"


# # Another child class (Polymorphism)
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Meow!"


# # Using the objects
# animals = [
#     Dog("Buddy"),
#     Cat("Milo")
# ]

# for animal in animals:
#     print(animal.speak())
