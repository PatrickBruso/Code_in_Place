""" Examples of OOP in python """


class Dog:      # Example of Dog class
    """
    Class attributes are used when you want the attribute to have the
    same value for all class instances.  They are always put first after
    the class name is created.
    """
    species = "Canis familiaris"

    """
    init is always used to set the initial state of the object and assign
    values to the object's properties.  All of the properties you want the
    class to have (name, age, etc) should be initialized with the init. You
    will always include "self" as this is used to pass the attributes to instances.
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    """
    Instance methods are functions defined inside a class and can only be called
    from an instance of that class.  The first parameter is always "self"
    """
    # def description(self):
        # print(f"{self.name} is {self.age} years old")

    def __str__(self):  # dunder method to replace description
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        print(f"{self.name} says {sound}")


# Create class instances
buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

print(f"{buddy.name} is {buddy.age} years old!")
print(f"{buddy.name} is a {buddy.species}!")

# Objects are mutable!
buddy.age = 10
print(buddy.age)
miles.species = "Felis silvestris"
print(miles.species)

# Use the instance methods
# buddy.description()
buddy.speak("Woof")
print(buddy)


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles."


Toyota = Car("blue", 85000)
Honda = Car("green", 60000)

print(Toyota)
print(Honda)


# Creating a child class of the Dog class for each breed
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):  # override the .speak() in the class definition for Dog
        return f"{self.name} says {sound}"


class Dachshund(Dog):
    def speak(self, sound="Bark"):
        return f"{self.name} says {sound}"


class Bulldog(Dog):
    def speak(self, sound="Woof"):
        return f"{self.name} says {sound}"


jack = Bulldog("Jack", 3)  # instantiate dogs using breed
print(jack)
print(type(jack))
print(isinstance(jack, Dog))  # check if jack is instance of Dog class using built in function
print(isinstance(miles, Bulldog))
