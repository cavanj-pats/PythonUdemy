# Circle Class - Challenge

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, radius):
        if radius >=0:
            self._radius = radius
        else:
            self._radius = 1

    @property
    def diameter(self):
        return self._radius * 2
    
    def area(self):
        return math.pi * self.radius * self.radius
    
    def perimeter(self):
        return math.pi * 2 * self.radius
    

c1 = Circle(5)
print (c1.area())

    
