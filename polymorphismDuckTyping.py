#polymorphismDuckTyping.py

#Polymorphism means "Many Forms"
#one name many forms
"""
    Duck Typing
    Method Overloading
    Method Overriding
    Operator Overloading
"""


class Tesla:
    def drive(self):
        print("Tesla Driving")

class Chevy:
    def drive(self):
        print("Chevy Driving")


class Duck:
    def talk(self):
        print("Duck Talking")
    
    def walk(self):
        print("Duck Walking")

class Dog:
    def talk(self):
       print("Dog Talking")
    
    def walk(self):
        print("Dog Walking")


def person(pet):
    pet.talk()
    if hasattr(pet, 'walk'):
        pet.walk()


def driver(car):
    if hasattr(car, 'drive'):
        car.drive()


#############################method overriding
class Parent:
    def show(self):
        print("Show Parent")

class Uncle(Parent):
    pass

class Child(Parent):
    def show(self):
        #super.show() is a way to call the parent function (un-remark it to test it.)
        print("Show Child")
####################################################    

ppet = Duck()
person(ppet)

car = Chevy()
driver(car)

unc = Uncle()
chld = Child()

unc.show()
chld.show()