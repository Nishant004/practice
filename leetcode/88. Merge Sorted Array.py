nums1 = [1,2,3,0,0,0]
nums2 =[2,5,6]
m = 3
n = 3


# nums1 = [1]
# m = 1
# nums2 = []
# n = 0

# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1

# nums1=[-1,0,0,3,3,3,0,0,0]
# m =6
# nums2 =[1,2,2]
# n =3

l=len(nums1)
p=len(nums2)
count =0

for i in range(l-1,m-1,-1):
        nums1[i] = nums2[count]
        count +=1
# nums1.sort()
print(nums1)
for i in range(l):
    for j in range(0,l-i-1):
        if nums1[j] > nums1[j+1]:
            nums1[j], nums1[j+1] = nums1[j+1], nums1[j]
            print(nums1)










# for i in range(len(nums1)-m):
#     for j in range(len(nums2)):
#         if (nums1[i] <= 0 or nums1[i] =="")and nums2[j] >=1:
#             nums1[i] = nums2[count]
#             count +=1
# print(nums1[:m])