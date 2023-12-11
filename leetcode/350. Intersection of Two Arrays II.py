nums1 = [4,9,5]
nums2 = [9,9,8,4]

# nums1=[1,2,2,1]
# nums2=[2,2]

# nums1 =[3,1,2]
# nums2 =[1,1]

list2=list()
dict1={}


for i in nums1:
    if i in dict1:
        dict1[i] +=1
    else:
        dict1[i] = 1
for j in nums2:
    if j in dict1 and dict1[j]>0:
        list2.append(j)
        dict1[j] -= 1
print(list2)
# for j in nums2:
#     if j in dict1:
#         if dict1[j] >0:
#             list2.append(j)
#             dict1[j] -= 1
#         else:
#             j +=1
# print(list2)


    # if dict1[j] <= 0:
    #     pass
    # dict1[j] -= 1
    # print(dict1)





    # if nums1[i] not in dict1:
    #     dict1[nums1[i]] = 1
    # else:
    #     dict1[nums1[i]] += 1

# for j in range(len(nums2)):
#     if nums2[j] in dict1:

# for j in dict1.values():

# print(list2)













# if len(nums1) > len(nums2):
#     for i in range(len(nums1)):
#         if nums1[i] not in dict1:
#             dict1[nums1[i]] = 1
#         else:
#             dict1[nums1[i]] += 1
#     print(dict1)
#     for j in range(len(nums2)):
#         if nums2[j] in dict1:
#             list2.append(nums2[j])
#     print(list2)
# else:
#     for j in range(len(nums2)):
#         if nums2[j] not in dict1:
#             dict1[nums2[j]] = 1
#         else:
#             dict1[nums2[j]] += 1
#
#     for i in range(len(nums1)):
#         if nums1[i] in dict1:
#             list2.append(nums1[i])
#     print(list2)


