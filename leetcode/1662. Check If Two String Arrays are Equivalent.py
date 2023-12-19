word1 = ["ab","c"]
word2 = ["a", "bc"]

str1=str()
str2=str()
for i in word1:
    str1 += i
for i in word2:
    str2 +=i
if str2==str1:
    print("True")
else:
    print("false")
# for i in range(0,len(word1)):
#     print(word1[i])
#     if word1[i] not in dict1:
#         dict1[word1[i]] = [i]
#     else:
#         dict1[word1[i]].append(i)
# print(dict1)