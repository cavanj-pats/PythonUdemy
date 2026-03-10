#108_rotateList.py
#due to added / removed content,   lecture numbers may have changed
# so this file and the lecture notes may have different numbers.


lst = [1,2,3,4,5,6,7]
n = 3   #number of rotations

rotated=lst[n:] + lst[:n]

print(f"Original List: {lst}")
print(f"Rotated list, rotated {n} times: {rotated}")

