# nums1 = [4,1,2]
# nums2 = [1,3,4,2]

# list1=[]
#
# for i in range(len(nums1)):
#     for j in range(len(nums2)):
#         if nums1[i] == nums2[j]:
#             s = nums1[i]
#             if s > nums2[j+1] :
#                 list1.append(-1)
#             else:
#                 list1.append(nums2[j+1])
#             print(list1)


nums1 = [2,4]
nums2 = [1,2,3,4]

# nums1 = [4,1,2]
# nums2 = [1,3,4,2]
list1 = []

for i in range(len(nums1)):
    found = False
    for j in range(len(nums2)):
        if nums1[i] == nums2[j]:
            found = True
        elif found and nums2[j] > nums1[i]:
            list1.append(nums2[j])
            break
    else:
        list1.append(-1)

print(list1)







