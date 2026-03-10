#leet26_RemoveDuplicatesSortedArray.py

#remove duplicates from sorted array such that
#items with duplicates appear no more than twice
class Solution:
    def removeDuplicates(nums):
        k = 0  #solution set size. for now use as trailing pointer
        i=1 # use as leading pointer
        #. count will be  number of elements
        count = 1
        loopCount = 0
        while i < len(nums) and loopCount<=len(nums):
            loopCount +=1
            
            if (nums[i] > nums[i-1]):
                #found new item
                k = i # at least this far are solution
                count = 1
                i += 1

            elif nums[i] == nums[i-1]:
                #found duplicate
                count +=1
                if count == 2 :
                    #this is 
                    k = i # this item is in the solution
                    i += 1
                elif count > 2:
                    #we do not want this item
                    v = nums.pop(i)
                    nums.append(v)
                    #i is now on the next item do not index i
                    # do not index k

            elif nums[i] < nums[i-1]:
                #we have reached start of items we've thrown away
                k = i-1
                break
        
        

        return k+1, nums
    



#. worked. nums = [0,0,0,1,1,1,1,2,3,3]; # Input array
# worked-- nums = [1,1,1,1,1,1,1,1,1]
nums = [0,0,1,1,2,2,2,3]
#expectedNums = [0,1,2,3,4]; # The expected answer with correct length

k, nums = Solution.removeDuplicates(nums); # Calls your implementation

print (nums)
print (k)

