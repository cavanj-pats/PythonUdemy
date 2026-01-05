#python
# positional versus keyword arguments
# positional is like classic C or C++ argument passed by position in the function definition
# keyword is like: volume(breadth=5, length=10, height=3)
# mixed is like:  volume(10.5, height = 3)  #positional argument cannot occur after keyword arg. 
#                                           # once you go keyword you apparently must stay keyword.
# postiional on left hand side and keyword on right hand side is the rule.
#guidance is to use positional or keyword but not both.


def volume (length, breadth, height = 1):
    print (length, breadth, height)
    return length * breadth * height


#print(volume(10,5,height=3))
    
#defulat arguments are crazy
# repeated calls of a function using the default arguments, where the function modifies the 
# default argument PERSIST.  They are created only the first time.
#    Check out the following:

""" def fun(l=[1,2,3]):
    l.append(len(l))
    print(l)


fun()
fun()
fun([10,11])
fun() """

# POsitional arguments
#   def fun(a,b,/,c,d)  #before / positional only.   After / positional OR Keyword.  if / is at the 
#  end all are positional.
# call   fun (5,10,15,d=20)  #this is acceptable
#   use a '*' for keyword only arguments.  putting '*' at the right end is wrong and will throw an error.

"""
def max3(a,b,c,/):
    if (a > b):
        if(a > c):
            return a
        else:
            return c
    else:
        if(b > c):
            return b
        else:
            return c
"""
        
#print(max3(10,6,5))


"""
def mx3(a,b,c,/):
    #this is abdul's code
    if (a > b) and (a > c):
        return a
    elif (b > c):
        return b
    else:
        return c
"""
"""
def simple_interest(*,P, T, R):
        # Principal  amount $$
        # T Time number of years
        # R is the interest rate per year
    return (P * T * R)/100


si = simple_interest(P=25000, T=4, R=5.49 )
"""


#Pangram phrase
import re


def pangram(phrase):
    letters = re.sub(r'[^a-zA-Z]','', phrase)
    letters_set = set(letters.lower())
    if len(letters_set) == 26:
        return True
    else:
        return False


str = 'The quick brown fox jumps over the lazy dog'
print (pangram(str))