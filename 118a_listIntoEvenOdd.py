# separate odd and even numbers

nums = input('Enter a list of integer numbers separated by a space: ')
L1 = nums.split()

even=[]
odd=[]

'''
    instructor used 
    odd =[x for x in L1 if L1 % 2 !=0]
    even = [x for x in L1 if x % 2 ==0]

    very simple!!

    instructor started with list of integers
    where i start with list of strings
    mine might require some additional manipulation
    nums = [int(x) for x in L1]   #very easy

'''
for element in L1:
    cFloatElement = float(element)
    if float(cFloatElement/2) == int(cFloatElement/2):
        even.append(int(element))
    else:
        odd.append(int(element))


print(f"L1: {L1}")
print(f"Even: {even}")
print(f"odd: {odd}")

