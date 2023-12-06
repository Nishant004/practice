heights = [180,165,170]
# heights = [17233,32521,14087,42738,46669,65662,43204,8224]
names = ["Mary","John","Emma"]
# names = ["IEO","Sgizfdfrims","QTASHKQ","Vk","RPJOFYZUBFSIYp","EPCFFt","VOYGWWNCf","WSpmqvb"]
# l=len(heights)
# for i in range(l):
#     for j in range(0,l-i-1):
#         if heights[i] > heights[i+1]:
#             heights[i],heights[i+1] = heights[i+1] ,heights[i]
# print(heights)

# n = len(heights)
# for i in range(n):
#     for j in range(0, n-i-1):
#         if heights[j] < heights[j+1]:
#             # Swap the elements if they are in the wrong order
#             heights[j], heights[j+1] = heights[j+1], heights[j]
#             names[i], names[i + 1] = names[i + 1], names[i]
#
# print(heights)
# print(names)
#             # names[i], names[i + 1] = names[i + 1], names[i]
#             # print(names)
dict1={}
# dict1=dict(zip(names, heights))
dict1={heights[i]: names[i] for i in range(len(heights))}
heights.sort(reverse=True)
list1=[]
for i in heights:
    if i in dict1:
        list1.append(dict1[i])
        print(list1)

