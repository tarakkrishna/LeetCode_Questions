class Solution(object):
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            while(nums[i]<len(nums)+1 and nums[i]>0 and i!=nums[i]-1):
                index=nums[i]-1
                temp=nums[i]
                nums[i]=nums[index]
                nums[index]=temp

        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1
"""Time limit exceeded"""