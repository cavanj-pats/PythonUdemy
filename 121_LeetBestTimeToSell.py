#121_LeetBestTimeToSell.py


class Solution(object):
    def maxProfit(nums):

        mx = 0
        for i in range(len(nums)-1):
            p = max(nums[(i+1):]) -nums[i]
            if p > mx:
                mx = p
        if mx < 0:
            mx = 0

        return mx


prices = [7,6,4,3,1]
s = Solution
print (s.maxProfit(prices))
