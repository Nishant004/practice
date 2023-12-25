nums = [2,0,1,0,3,12]

# nums=[1,0,1]

n = len(nums)
i = 0
j = 0


while i < n :
    if nums[i] != 0 :
        nums[i], nums[j] = nums[j], nums[i]
        j += 1
    i +=1
print(nums)

# while j < len(nums):
#     if nums[j] != 0:
#         nums[i], nums[j] = nums[j], nums[i]
#         i += 1
#     j += 1
#
# print(nums)

# while i < n and j < n:
#     if nums[i] == 0 and nums[j] != 0:
#         nums[i], nums[j] = nums[j], nums[i]
#         i += 1
#     j += 1
#
# print(nums)


# while i < len(nums):
#     if nums[i] == 0 and nums[j] != 0:
#         nums[i], nums[j] = nums[j], nums[i]
#         i += 1
#     else:
#         j +=1
# print(nums)
