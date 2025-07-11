class Solution(object):
    def containsDuplicate(self, nums):
        for i in nums:
            count = 0
            for j in nums:
                if i == j:
                    count += 1
            if count >= 2:
                return True
        else:
            return False


