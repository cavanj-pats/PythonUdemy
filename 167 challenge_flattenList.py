# flatten a list
#challenge
#has nested lists

def flatten(L):
    for ele in L:
        if type(ele)==list:
            flatten(ele)
        else:
            print (ele, end=', ')
            #next(ele)



theList = [1,3,4,[5,6,[7,8],9],10]
flatten(theList)


"""
abdul code

def flatten(L):
    for e in L:
        if hasattr(e, '__iter__'):
            yield from flatten(e)
        else:
            yield e


f = flatten([1,2,[3,[4,5],6,7],8])

print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

"""