#leet26_RemoveDuplicatesSortedArray.py



def removeDuplicates(nums):
        k = 0  #count of unique elements
        i=1

        while i in range(1, len(nums)):
            #move i along the index
            if(nums[k] == nums[i]):
                #index i,  keep k alone
                v = nums.pop(i)
                nums.append(v)
                
            elif nums[i] >= nums[k]:
                k+=1
                i+=1
            else:
                 break


        return k, nums
    



nums = [0,0,1,1,1,2,2,3,3,3,4]; # Input array
#expectedNums = [0,1,2,3,4]; # The expected answer with correct length

k, nums = removeDuplicates(nums); # Calls your implementation

print (nums)
print (k)

