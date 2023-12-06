nums = [2,3,1,2,4]
count=0
n=len(nums)

even = [x for x in nums if x % 2 == 0]
odd = [x for x in nums if x % 2 != 0]

total = even + odd
print(total)

