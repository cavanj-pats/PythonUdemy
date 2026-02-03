#create and raise user defined exception

class NegativeError(Exception):
    pass

class betterNegError(Exception):
    def __init__(self):
        self.msg = 'Dimensions cannot be less than zero!'
    def __str__(self):
        return self.msg
    

def Area(l, w):
    if l >=0 and w>= 0 :
        return l*w
    else :
        #raise NegativeError('Dimensions cannot be less than zero!')
        raise betterNegError()
    


print(f"Area =: {Area(1, -5)}")
