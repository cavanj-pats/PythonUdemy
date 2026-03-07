#350_NumPY_Intro.py


import numpy as np

arr = np.array([2,4,6,8])
arr2 = np.array([[10,12,14,16],[9,11,13,15]])
arr3 = np.zeros((3,4,5)) # 3 planes 4 rows 5 columns
arr4 = np.linspace(5,12,num=6)
arr5 = np.arange(1,18,2)
arr6= np.eye(3) #identity matrix
arr7 = np.diag((2,4,6,8))

print('\n')
print(f"np.linspace(0,10,num=5): {arr4}")

print(f"NP arange(1,18,2): {arr5}")

print(f'\nnp.eye(3):\n {arr6}')
print('\nnp.diag((2,4,6,8)):')
print(f"{arr7}")

print(f"arr[1:4]: {arr[1:4]}")

print(f"arr2[0:2, 1:3]{arr2[0:2, 1:3]}")

print(arr)
print(arr[1])

print("arr2:")
print(arr2)
print(arr2[1][1])
print("arr[1:4:2, 1:4:2]")
print(arr2[1:4:2, 1:4:2]) 
