#objectVectorOpOverloading.py

#parent type classes can be
# Concrete classes - have some or all of the intended functionality that child classes access
# Interface - function interfaces are defined by functionality is deferred to child.
#abstract - mixture of Concrete and Interface 


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    #overload the built in addition operator
    #abdul said if you call it using '+' it will invoke this function
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    #this is how to create a function to be used when "print" is invoked
    def __str__(self):
        return f"({str(self.x)},{str(self.y)})"



v1 = Vector(2,2)
v2 = Vector(1,5)
v3 = v1+v2
#print(v3.x, v3.y)
print(v3)