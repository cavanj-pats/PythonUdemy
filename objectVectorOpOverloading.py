#objectVectorOpOverloading.py



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
    



v1 = Vector(2,2)
v2 = Vector(1,5)
v3 = v1+v2
print(v3.x, v3.y)