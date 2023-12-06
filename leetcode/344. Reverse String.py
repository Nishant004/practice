s = ["H","a","n","n","a","h"]
# n=len(s)
# rev= []
# for i in range(n-1,-1,-1):
#
#     rev.append(s[i])
#
# print(rev)

left, right = 0, len(s) - 1

for i in range(len(s) // 2):
    temp = s[left]
    s[left] = s[right]
    s[right] = temp
    left += 1
    right -= 1

print(s)