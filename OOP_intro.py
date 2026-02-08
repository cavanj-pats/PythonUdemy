
#
#   introduction to objects
"""
    Class hs
        Properties  / Data Members
        Methods   /  Member Functions
        
        this achieves
            encapsulation
            abstraction
            data hiding
            
            ...
            inheritance
            polymorphism
"""

#init method is the Constructor method
#Python does not support multiple constructors or overload functions like C++
# instead you can provide default arugments....i forgot about that.
# normally it is best to create instance variables within __init__.
# you *can* create an instance variable in another function
# but you must call the other function before trying to access the instance variable.
#   *** this is dangerous from an error standpoint
#    abdul also created an instance variable from the main function by simply referring to a variable and giving it a value.
#   this is very error prone i would think.


class Rectangle:
    #class variables are not same as instance variables
    #for example count below is meant to count number of instances of a Rectangle object have been intantiated
    #accessible to all instances
    """
        Docstring for Rectangle
        class Variables
            Declared outside of all methods
            created only once, common to all instances
            Can be accessed using object or class name
            Used as Shared Data
            Stores information about class (Meta Data)
            class variables are also STATIC variables

        class Methods
            decorator @classmethod is used
            first parameter is 'cls' class variable
            access only class variables
            Can be called using an instance or class name

        Static Methods
            utility functions
            ca't be called using class name
            can't access members of a class
            @staticmethod decorator is used 

        Property Methods
            I think these will be your get and set methods  (I was right)
            but.....
            ._length  means protected
            we want to be able to say r.length = x and be able to assign a length 
            yet have the set code be what sets the length
            ....yet length will be protected
            @property -> for get
            @propertyname.setter for set method

            Private data
            use double underscore in name,  aka dunder
            .data instead call it .__data
            can only access Private data  using name Mangling
            ._Rectangle.__length for example will force access to the Private data member length

            Protected data
            use single underscore

                        public.     protected.   private
        Inside Class      Y.             Y.         Y
        Child Class.      Y               Y         N
        Using Object      Y             Y           N

    """
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
    
    
    
r = Rectangle()
q = Rectangle(5,9)

print (r.area())
print (q.area())
r.length = 100
print (r.area())
print (Rectangle.get_count())
print (Rectangle.get_area(9,8))






"""
    These are the old getters adn setters before makeing them properties

    def set_length(self, len):
        if len >=0 :
            self.length = len
        else:
            self.length = 1
    
    def get_length(self):
        return self.length
    
    def set_breadth(self, br):
        if br >= 0:
            self.breadth = br
        else:
            self.breadth = 1

    def get_breadth(self):
        return self.breadth
"""