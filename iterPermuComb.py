# itertools  combinations permutations 
#not sure if there is a combination generator


from itertools import permutations
from itertools import combinations
from itertools import product

#and for statistics
import statistics
#mean, median, mode - udemy example


list1 = [0,1,2,3,5,5]
list2 = ['a','b']

#the functions do not return an iterable list.  i'm not sure what they return
# you can convert them into a list by using the list() function
# p = permutations(list1,2)  p_list = list(p)

for l in combinations(list1, 2):
    print (l)

print ('\n')

for z in permutations(list1,2):
    print(z)

for p in product(list1,list2):
    print(p)


print (f'List1 mean: {statistics.mean(list1)}')
print (f'List1 median: {statistics.median(list1)}')
print (f'List1 mode: {statistics.mode(list1)}')