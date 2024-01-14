nums = [4,5,5,5,2,2]
k = 2

dict1={}
list1=[ [] for i in range(len(nums)+1)]

if k == 0:
    print("0")
for i in range(len(nums)):
    if nums[i] not in dict1:
        dict1[nums[i]] = 1
    else:
        dict1[nums[i]] +=1
# print(dict1)
res=[]
for i , c in dict1.items():
    list1[i].append(c)
    print(list1)
    res.append(i)
    if len(res)==k:
        print(res)


# print(list1)
