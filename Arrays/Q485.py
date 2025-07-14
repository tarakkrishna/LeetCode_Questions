class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        max = 0
        for i in nums:
            if i == 1:
                count += 1
                if max < count:
                    max = count
            else:
                count = 0
        return max
