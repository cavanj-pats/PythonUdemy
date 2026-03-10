#leet26_RemoveDuplicatesSortedArray.py

#remove duplicates from sorted arrach such that
#items with duplicates appear no more than twice
class Solution:
    def removeDuplicates(nums):
        k = 0  #solution set size. for now use as trailing pointer
        i=1 # use as leading pointer
        #. count will be  number of elements
        count = 1

        while i in range(1, len(nums)):
            #move i along the index
            if(nums[k] == nums[i]):
                #index i,  keep k alone
                count += 1
                if count > 2 :
                    v = nums.pop(i)
                    nums.append(v)
                else:
                    k += 1
                    i += 1
                
            elif nums[i] >= nums[k]:
                count = 1
                k+=1 
                i+=1
            else:
                 break


        return k+1, nums
    



nums = [0,0,0,1,1,1,1,2,3,3]; # Input array
#expectedNums = [0,1,2,3,4]; # The expected answer with correct length

k, nums = Solution.removeDuplicates(nums); # Calls your implementation

print (nums)
print (k)

