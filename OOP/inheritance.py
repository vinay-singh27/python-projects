##Inheritance

'''
Inheritance is a way to form new classes using classes that have already been defined. 
The newly formed classes are called derived classes, the classes that we derive from are called base classes. 
Important benefits of inheritance are code reuse and reduction of complexity of a program. 
The derived classes (descendants) override or extend the functionality of base classes (ancestors).
'''

class Animal:
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")

d = Dog() #This will initiate a Dog class as wells as Animal class