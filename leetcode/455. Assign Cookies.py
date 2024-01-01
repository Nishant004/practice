# g = [1,2,3]
# s = [1,1]
import math


# g=[1,2,3]
# s= [3]

# g = [1,2]
# s = [1,2,3,5,6,7,8]

g=[1,2,3]
s=[1,1]

count=0
n = len(s)

# for i in range(len(g)):
#     if n != 0:
#         count +=1
#         n -=1
#     else:
#         break
# print(count)



# g.sort()
# s.sort()

i, j = 0, 0
while i < len(g) and j < len(s):
    if g[i] <= s[j]:
        count += 1
        i += 1
    j += 1

print(count)
