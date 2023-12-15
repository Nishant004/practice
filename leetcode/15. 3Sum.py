# nums = [-1,0,1,2,-1,-4]
nums = [0,0,0]
if len(nums) < 3:
    print([])

nums=sorted(nums)
# [-4, -1, -1, 0, 1, 2]
res=[]
for i in range(0,len(nums)-2):
    if nums[i] > 0:
        break
    if nums[i] == nums[i-1] and i > 0:
        continue
    low = i+1
    high = len(nums)-1

    while low < high :
        s = nums[i] + nums[low] + nums[high]

        if s == 0:
            res.append((nums[i],nums[low],nums[high]))

        if s <= 0:
             low +=1
             while(nums[low] == nums[low-1] and low < high):
                 low +=1
        else:
            high -=1
print(list(set(res)))


# res=[]
# for i in range(0,len(nums)-2):
#     for j in range(i+1,len(nums)-1):
#         k = -(nums[i] + nums[j])
#         if k in nums and i != k and j != k  and k + nums[i] + nums[j] == 0  :
#             res.append(tuple(sorted([nums[i],nums[j],k])))
# print(res)
# print(list(res))
        # and nums[i] != nums[j]
        #  and j != k and i != k and i != j  and k != nums[i] and k != nums[j] :




