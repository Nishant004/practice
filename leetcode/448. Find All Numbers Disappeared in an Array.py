nums = [4,3,2,7,8,2,3,1]
# missing=[]
# set1=set(nums)
#
# for i in range(1,len(nums)+1):
#     if i not in set1:
#         missing.append(i)
# print(missing)

print (list(set(range(1,len(nums)+1))-set(nums)))