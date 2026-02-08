#class Cuboid

from classRectangle import Rectangle

class Cuboid(Rectangle):
    def __init__(self, l, b, h):
        self.height = h
        super().__init__(l, b)

    def volume(self):
        return self.height * self._length * self._breadth
    

c = Cuboid(4,5,2)
print(c.volume())