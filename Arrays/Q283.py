class Solution(object):
    def moveZeroes(self, nums):
        n=0
        for i in nums: #this iterates over a snapshot even if the list is changed the i iterates over the original snapshot
            if i==0:
                n=nums.pop(nums.index(i))
                nums.append(n)
        return nums