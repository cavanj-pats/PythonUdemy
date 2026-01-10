#Closure functions
# has nested function
# returns a function
# inner function accesses outer function variables

def Outer():     #outer function is the closure function
    msg = 'Welcome'
    def Inner():
        print('+' * 10)   #print + ten times
        print(msg)
        print('+' * 10)

    return Inner
    #nested and returns it is a closure

def Wobble(msg):     #outer function is the closure function
    def Inner():
        print('+' * 20)   #print + ten times
        print(msg)
        print('+' * 20)

    return Inner
    #nested and returns it is a closure



f = Outer()
f()
print('\n')
g=Wobble('Wobble Function')
g()

print('\n')


count = 0
def counter():
    global count   #so global counter variable can be accessed
    count +=1
    return count

def get_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter



#c1 = counter()
c2 = get_counter()

print(counter(), counter(), counter())
print(c2(),c2(), c2())

