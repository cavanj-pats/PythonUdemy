#reverseList.py

idx = int(input('Enter index for list rotation: '))

list = [0,1,2,3,4,5,6,7]

l2 = list[idx:] + list[0:idx]

print(list)
print(l2)

