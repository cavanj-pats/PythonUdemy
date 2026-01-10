#decoratorFunction.py

#closure function that takes function as a parameter
def Outer(f):
    def Inner():
        print('+' * 10)   #print + ten times
        f()
        print('+' * 10)

    return Inner

@Outer    #Outer is the "decorator function"
def display():
    print('Welcome!')

#r = Outer(display)
#r()

#display = Outer(display)
display()

