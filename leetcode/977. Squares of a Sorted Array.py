nums=[-4,-1,0,3,10]
ne=[]
for i in range(len(nums)):
    nums[i] *=nums[i]
    ne.append(nums[i])
print(sorted(ne))