#next month challenge


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

def next_month():
    m = ['January', 'February','March','April','May','June','July','August','September','October','November','December']
    i=0
    while True:
        yield m[i]
        i = (i+1) % 12


m_month = next_month()
next(m_month)
print(next(m_month))  #should print February


"""
import calendar
def next_month():
    count = 0
    while True:
        name = calendar.month_name[count]
        yield(name)
        count = count % 12 +1  #when using built in

m = next_moth()
print(next(m))
print(next(m))



"""