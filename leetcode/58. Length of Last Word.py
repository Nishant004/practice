s = "Hello World    "
n=len(s)
count=0
space=0
for i in range(n-1,-1,-1):

    if s[i] == " ":
        if count==0:
            continue
        else:
            break
    else:
        count +=1
print(count)

# n = len(s)
# count = 0
# spaceagain = False
# for i in range(n - 1, -1, -1):
#     if spaceagain:
#         if s[i] != " ":
#             count += 1
#         else:
#             break
#     else:
#         if s[i] == " ":
#             count += 0
#         else:
#             spaceagain = True
#             count += 1
# return count