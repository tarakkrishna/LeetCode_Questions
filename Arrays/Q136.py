class Solution(object):
    def singleNumber(self, nums):
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for i in dic:
            if dic[i] == 1:
                return i
