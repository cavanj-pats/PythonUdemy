#fibonacci.py


fib = int(input("Enter the fibonacci Term you want: "))
result = {}
result[0] = 0
result[1] = 1


for x in range(0, fib):
    result[x+2] = result[x] + result[x+1]


print("Fibonacci of ", fib, " equals: ", result[fib])

a = 0
b = 1
for y in range(0, fib):
    c = a + b
    a = b   #answer is stored in a. staring point is 0 and loop will stop after fib-1 term
    b = c

print (a)    

