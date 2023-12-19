nums = [5,6,2,7,4]

nums=sorted(nums)
n=len(nums)
for i in range(n):

    a=nums[n-1]
    b=nums[n-2]
    c=nums[1]
    d=nums[0]
    s=(a * b) - (c * d)
print(s)