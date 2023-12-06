# h=haystack = "dsabsad"
# n=needle = "sad"
# i=0
# count=0
#
# if len(h)<len(n):
#     print(-1)
#
# while i<len(h):
#     if count == len(n):
#         break
#     if n[i]==h[i]:
#         count +=1
#         i += 1
#     else:
#         h[i] +=1
#         n[i] *=0
#         count
# print(count)
h = "sabsad"
n = "sad"
i = 0
count = 0

if len(h) < len(n):
    print(-1)

while i < len(h):
    if count == len(n):
        break
    if n[count] == h[i]:
        count += 1
        i += 1
    else:
        i = i + 1
        count = 0
if count == len(n):
    print(i - count)
else:
    print(-1)

