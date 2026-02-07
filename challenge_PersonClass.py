#person

class ValueError(Exception):
    pass

from datetime import date

class Person:
    def __init__(self, first, last, year):
        self.__fname = first
        self.__lname = last
        self.__yob = year


    @property
    def name(self):
        return f'{self.__fname} {self.__lname}'

    @name.setter
    def name(self, name):
        #must separate full name
        #if a name is missing throw exception
        names =name.strip().split()
        if len(names) !=2:
            raise ValueError("Full Name must contain First and Last Name!")
        self.__fname = names[0]
        self.__lname = names[1]

    @property
    def age(self):
        #need date class to determine age
        return date.today().year - self.__yob



jim = Person('Jim', 'Cavanaugh', 1966)

print(jim.age)
jim.name = 'James Johnson'
print(jim.name)
