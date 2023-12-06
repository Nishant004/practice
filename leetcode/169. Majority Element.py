nums = [6,5]
dict1={}


for i in nums:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1


max_num = None

for j in dict1:
    if max_num is None or dict1[j] > dict1[max_num]:
        max_num = j
print(max_num)