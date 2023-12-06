nums = [1,3,5,6]
target = 7
# nums.append(target)
nums = nums + [target]

sh=sorted(nums)
for i in range(len(sh)):
    if sh[i] == target:
        print(i)

