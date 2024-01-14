strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
dicts ={}
for word in strs:
    sorted_word = ''.join(sorted(word))
    dicts[sorted_word]= dicts.get(sorted_word,[]) +[word]
print(dicts.values())




# strs = ["eat","tea","tan","ate","nat","bat"]
# # strs = ["tea","tan","ate","nat","bat","eat"]
# #        ["tea","ate","tan","nat","bat","eat"]
# #        ["tea","ate","eat","tan","nat","bat"]
# s = len(strs)
# i = 0
# j=1
# k=1
# list1=[]
#
# while i < s :
#     for x in set(strs[i]):
#         if (strs[i].count(x)) != (strs[j].count(x)):
#             j +=1
#         else:
#             if j == (s-1) :
#                 strs[j], strs[k] = strs[k], strs[j]
#                 i = k
#                 j = i+1
#                 k=j
#                 list1.append(strs[:i])
#                 break
#             else:
#                 strs[j],strs[k]=strs[k],strs[j]
#                 k = j
#                 j +=1
# print(list1)
#
#


        # if x not in dict1:
        #     dict1[i[x]] = 1
        # else:
        #     dict1[i[x]] +=1

