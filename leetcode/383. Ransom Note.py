m=magazine = "aabd"
r=ransomNote = "aa"

dict1={}

if len(r)>len(m):
    print("False")

for i in m:
    if i in dict1:
        dict1[i] +=1
    else:
        dict1[i] = 1

for alpha in r:
    if alpha not in  dict1:

        print("FalseX")

    if dict1[alpha] <=0:

        print("falseY")

    dict1[alpha] -=1

print("True")
print(dict1)







# if len(ransomNote)>len(magazine):
#     print ("False")
# dict1={}
#
# for i in magazine:
#     if i in dict1:
#         dict1[i] +=1
#     else:
#         dict1[i] = 1
#
# for char in ransomNote:
#     if char not in dict1:
#         print("False")
#     if dict1[char] <= 0:
#         print("False")
#
#     dict1[char] -=1
# print("True")
# print(dict1)

















# y=sorted(magazine)
# x=sorted(ransomNote)
# er=str()
#
# for i in range(len(y)):
#     for i in range(len(x)):
#         if y[i]==x[i]:
#             # print("True")
#            er += y[i]
#         break
# print(er)
# # if er != x:
# #     print("True")
# # else:
# #     print("False")
#
