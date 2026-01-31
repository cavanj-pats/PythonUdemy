#python
# positional versus keyword arguments
# positional is like classic C or C++ argument passed by position in the function definition
# keyword is like: volume(breadth=5, length=10, height=3)
# mixed is like:  volume(10.5, height = 3)  #positional argument cannot occur after keyword arg. 
#                                           # once you go keyword you apparently must stay keyword.
# postiional on left hand side and keyword on right hand side is the rule.
#guidance is to use positional or keyword but not both.

"""
Docstring for functionNotesPractice
def volume (length, breadth, height = 1):
    print (length, breadth, height)
    return length * breadth * height

"""

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

"""
def pangram(phrase):
    letters = re.sub(r'[^a-zA-Z]','', phrase)
    letters_set = set(letters.lower())
    if len(letters_set) == 26:
        return True
    else:
        return False


str = 'The quick brown fox jumps over the lazy dog'
print (pangram(str))
"""


"""
Variable length position arguements
def fun (*args)    content of args will be a tuple

Variable length keyword arguments
def fun (**kwargs)   content of kwargs wll be dicitonary
no arguments allowed after variable length keyword arguments
arguments are allowed before variable length keyword argument.
these preceding arguments can be either positional or keyword.

def fun(*args, a, b, **kwargs)    only if a, b are keyword arguments. Not allowed if a.b are positional


"""
"""
#variable length keyword arguments
def fun(*args, a, b, **kwargs):
   print (args, a, b, kwargs)
   # for item in kwargs.items():
   #     if item[0]=='b':
   #         print(item[1])   #print only the value in b.   item will be a key:value tuple

fun(3,4,a = 6, b=5, c=10, d=11)


#can return multiple values from a function
def mult(a, b, c):
    sum = a + b + c
    prod = a * b * c
    return sum, prod

print(mult(4,3,9))


#grade scorer returns total, average and pass/fail
def results( *marks):
    item_count = len(marks)    #how many grades were submitted
    total = 0
    for item in marks:
        total +=  int(item)

    average = total/item_count

    if (average >= 60):
        grade = 'Pass'
    else:
        grade = 'Fail'

    return total, average, grade

print(results(55, 75, 95, 90))


def unique_nums(*args):
    nums = set(args)  #convert tuple to set
    return list(nums)    #convert nums to list


#print (unique_nums(5, 2, 7, 5, 4, 0, 7, 9, 12))

#in Abdul's example he took input from user which was a string of numbers.  
#  use split to get the individual numbers as an integer
#print("Enter numbers seprated by spaces: ")
nums = "5 4 3 7 5 1 7 11"   #input("")
numbers = [int(n) for n in nums.split()]  #puts in a list
unique = unique_nums(*numbers)    #this is how you must pass the arguments.  (this is new)

print("\nUnique Numbers: ")
print(unique)
           

"""


"""
# when it came to testing, this function worked. When it came to grading, this function
#did not work.  I gave up trying to deterine why.  i simply pasted in Abdul's code for the grading
def is_strong(password):
    special_chars = set("!@#$%^&*-_+=.")

    msg = 'Password must contain '
    if len(password)<8:
        return False, msg + "at least 8 characters"
    if not any(c.isupper() for c in password ):
        return False, msg + "one UPPERCASE character"
    if not any(c.islower() for c in password ):
        return False, msg + "one lowercase character."
    if not any(c.isnumeric() for c in password):
        return False, msg + "one number."
    if not any(c in special_chars for c in password):
        return False, msg + "special characters."
    
    return True, 'Password is Strong'


print (is_strong('Applebannana9'))
"""

"""
################################## THIS IS ABDULS CODE   ##############################
def is_strong(password):
    msg = 'Password must contain at least'
    if len(password) < 8:
        return False, msg + " 8 characters"

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    special_chars = set("!@#$%^&*-_+=")
    has_special = any(c in special_chars for c in password)

    if not has_upper:
        return False, msg + " one uppercase letter."
    if not has_lower:
        return False, msg + " one lowercase letter."
    if not has_digit:
        return False, msg + " one digit."
    if not has_special:
        return False, msg + " one special char (!@#$%^&*-_+=)"

    return True, "Password is strong!"

password = input("Enter your password: ")
valid, message = is_strong(password)
print(message)

###################.    END OF ABDULS CODE.  #########################
"""


"""
# this seems like we made our own interator function
def myrange(n):
    i = 0
    while (i<n):
        yield i
        i = i + 1


n = myrange(4)

print(next(n))
print(next(n))
print(next(n))
print(next(n))
"""


"""
##He refers to this as a generator
# prepare a function that will cycle through the days of the week
# each invokation of next() will move to the next day.
# I am not sure how it establishes the range when the loop is infinite

def days():
    d = ['Sun', 'Mon', 'Tues', 'Wed', 'Thu', 'Fri', 'Sat']
    i = 0
    while True:
        yield d[i]
        i = (i +1) % 7   # mod 7 returns to i = 0


d = days()
next(d)
print(next(d))    #should print Mon
"""



"""
def rec(n):
    if(n>0):
        print(n)
        rec(n-1)

    print(n)
rec(4)
"""

"""

def factorial(n):
    if(n<=0):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))
"""


def fib_term(n):
    a,b = 0,1   #first two terms of Fibonacc sequence

    for i in range(n+1):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    num = 10

    for term in fib_term(num):
        print(term, end = ', ')
        
    print("\n")

