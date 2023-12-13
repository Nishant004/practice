nums = [3,4,5,2]
s=0

for i in range(0,len(nums)-1):
    for j in range(i+1,len(nums)):
        storge = (nums[i]-1)*(nums[j]-1)
        if storge > s:
            s=storge
print(s)