#return a function from a funtion. This is cool but could become difficult to manage

def Outer():

    def Inner():
        print('Welcome!')

    return Inner


f = Outer()

f()


