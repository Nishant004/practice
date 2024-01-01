# s = "egg"
# t = "add"

# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         return self.mask(s) == self.mask(t)
#
#     def mask(self, text: str):
#         d = {}
#         msk = []
#         for i in range(len(text)):
#             if text[i] in d:
#                 msk.append(d[text[i]])
#
#
#             else:
#                 d[text[i]] = i
#                 msk.append(i)
#             print(d)
#         return msk
#
# bje=Solution()
# print(bje.isIsomorphic("egg","add"))
# print(bje.mask("add"))
# print(bje.mask("egr"))

s = "egg"
t = "add"

dict1={}
dict2={}
mark=[]
mark2=[]

for i in range(len(s)):
    if s[i] in dict1:
        mark.append(dict1[s[i]])
    else:
        dict1[s[i]] = i
        mark.append(i)
for j in range(len(t)):
    if t[j] in dict2:
        mark2.append(dict2[t[j]])
    else:
        dict2[t[j]] = j
        mark2.append(j)


if mark == mark2:
    print("True")
else:
    print("False")