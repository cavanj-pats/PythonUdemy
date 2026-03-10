#58_FindMaxMin_Loop.py


i=0
x= [22,5,98,3, 1,-1,64]

n = len(x)
max = float('-inf')
min = float('inf')

while (i<n):
    if x[i]>max:
        max = x[i]
    
    if x[i]<min:
        min = x[i]

    i+=1


print(f"Max: {max}")
print(f"Min: {min}")
