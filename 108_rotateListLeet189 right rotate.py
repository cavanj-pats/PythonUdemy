#108_rotateList.py
#due to added / removed content,   lecture numbers may have changed
# so this file and the lecture notes may have different numbers.
#in-place rotation
#right rotate

# the below shows my solution along with a couple solutions from the comments.

#From Leetcode solution comments
#there were objections to this due to the extra memor needed
class Solution(object):
   def rotate(nums, k):
       # Get the actual number of rotations
       k = k % len(nums)      
       # Get the number of elements to move from the end to the beginning
       r = len(nums) - k
       # Store the elements to move
       new = nums[0:r]
       # Remove the elements from the beginning
       nums[0:r] = []
       # Append the stored elements to the end
       nums.extend(new)

class Solution2(object):
    def rotate(nums, k):
        if k == 0:
            return #i suppose this is smart but i wonder if k=k%len(nums) is smarter to do first
        
        size = len(nums)
        k = k if k <= size else k % size
        #i'd say to move k == 0 return here
        
        nums[k:], nums[:k] = nums[:size - k], nums[size - k:]




#this code works but is not the most effecient for speed and memory
#it is perfectly acceptable.
#not optimal for large values of k and when k >len(nums)
#i had some attempt to make different values of k loop more efficiently.
#could have been better had I used modular arithmetic

#nums = [1,2,3,4,5,6,7]
nums = [1,2,3]
print(f"Original List: {nums}")
k = 7   #number of rotations to the right
size = len(nums)
flag = False

# if k == size do nothing 
#if k > size then it is going to require looping
if k < size:
    v = size - k
elif k > size:
    v = k
else:
    flag = True

for i in range(0,k):
    if flag == True:
        break
    
    tmp = nums.pop()
    nums.insert(0, tmp)




#rotated=lst[n:] + lst[:n]


print(f"Rotated list, rotated {k} times: {nums}")
print(nums[-1])

## the below uses the leetcode solution so i can step through and see it work.
s = Solution
nums = [1,2,3]
print (f"original nums: {nums}")
s.rotate(nums, k)

print(f"Rotated list, rotated {k} times: {nums}")
print(nums[-1])

s2 = Solution2
nums = [1,2,3]
print (f"original nums: {nums}")
s2.rotate(nums, k)

print(f"Rotated list, rotated {k} times: {nums}")
print(nums[-1])