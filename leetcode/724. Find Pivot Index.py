nums = [1,7,3,6,5,6]
n = len(nums)

total_sum = 0
for num in nums:
    total_sum += num

leftside = 0
rightside = total_sum
pivot_index = -1

for i in range(n):
    rightside -= nums[i]
    if leftside == rightside:
        pivot_index = i
        break
    leftside += nums[i]

print(pivot_index)





