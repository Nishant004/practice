# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#
# s1 = "ab"
# s2 = "eidbaooo"
#
# s1 = "ab"
# s2 = "eidboaoo"

s1="abe"
s2="babae"


# i = 0
list3=sorted(s1)
dict1={}
dict2={}
list1=[]
j=0
for i in range (len(s1)):
    if s1[i] not in dict1:
        dict1[s1[i]] = 1
    else:
        dict1[s1[i]] +=1
while j <len(s2):
    

        # if (sorted(s2[j-1:len(s1)]) == sorted(s1[0:len(s1)])):
        #     print("true")
            # j +=1
            # print(sorted(s1[0:len(s1)]),"1")
            # print((s2[j-1:len(s1)]),"2")
#         else:
#             j +=1
#             # print("ture")
# print("false")
#             # if s2[j] in s2[j:len(s1)]:


#         else:
#             j +=1
# print("flase")






