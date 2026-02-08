# class Rectangle

class Rectangle:
    
    count = 0
    
    
    def __init__(self, l=1, b=1):
        self.length = l
        self.breadth = b
        Rectangle.count += 1          #this is where you index the class variable count.   Need to use Classname
    
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, len):
        if len >=0 :
            self._length = len
        else:
            self._length = 1
    
    @property
    def breadth(self):
        return self._breadth
    
    @breadth.setter
    def breadth(self, br):
        if br >= 0:
            self._breadth = br
        else:
            self._breadth = 1

        
    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
    #use decorator to note this as a class method
    #if you don't use teh decorator you can access this from each instance.
    #it works but perhaps is prone to errors.  Better to accesss using the class name
    @classmethod
    def get_count(cls):
        return cls.count
    
    ## static Method can be available even if you don't have an instance
     # used example of valuation of car without buying a car
     # or calculating interest without having an account

    @staticmethod
    def get_area(length, breadth):
        return length * breadth
    
  