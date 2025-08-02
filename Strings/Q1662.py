nums=list(set([3,2,1]))
max1=nums[0]
max2,max3=0,0
for i in nums:
    if i>=max1:
        max3=max2
        max2=max1
        max1=i
if len(nums)<3:
    print(max1)
print(max3)