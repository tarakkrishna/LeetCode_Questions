class Solution(object):
    def sortedSquares(self, nums):
        y=0
        for i in nums:
            nums[y]=i*i
            y+=1
        return sorted(nums)