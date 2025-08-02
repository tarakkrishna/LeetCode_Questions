class Solution(object):
    def thirdMax(self, nums):
        nums = list(set(nums))
        max1 = float('-inf')
        max2, max3 = float('-inf'), float('-inf')
        for i in nums:
            if i > max1:
                max3 = max2
                max2 = max1
                max1 = i
            elif i > max2:
                max3 = max2
                max2 = i
            elif i > max3:
                max3 = i
        if max3 == float('-inf'):
            return max1
        return max3
