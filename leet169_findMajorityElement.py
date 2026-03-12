#leet26_RemoveDuplicatesSortedArray.py

#remove duplicates from sorted array such that
#items with duplicates appear no more than twice
class Solution:
    def majorityElement(nums):
        d = dict()
        n = len(nums)
        for item in nums:
            d[item] = d.get(item, 0) + 1 # get won't throw an error if item does not exist
                #alse you don't need to check if d[item] is None this safeguards against error

            #since majority element is the one found n/2 times or greater just.perofrm the check    
            if d[item] >n//2:
                return item  #can stop here since there will always be a majority item. otherwise rturn None
    



#. worked. nums = [0,0,0,1,1,1,1,2,3,3]; # Input array
# worked-- nums = [1,1,1,1,1,1,1,1,1]
nums = [0,0,2,2,2,2,2,3]
#expectedNums = [0,1,2,3,4]; # The expected answer with correct length

k  = Solution.majorityElement(nums); # Calls your implementation

print (nums)
print (k)

