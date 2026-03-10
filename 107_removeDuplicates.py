#remove duplicates from a list


strInput = input('Enter a list of items separated by a space: ')
L1 = strInput.split()
res=[]
for i in L1:
    if not (i in res):
        res.append(i)
        
res.sort()

print(res)


