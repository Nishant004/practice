nums = [3,2,1,5,4]
k = 2

i=0
count=0

while i<=len(nums):
    if nums[i+1] - nums[i] == k:
        count +=1
        i +=1

print(count)