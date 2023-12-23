s = "1011101"
zero=0
one=s.count('1')
res=0

for i in range(len(s)-1):
    if s[i] == '0':
        zero +=1
    else:
        one -=1
    res=max(res,one+zero)
print(res)


# split = 1
# maxcount=0
#
# while len(s) > split:
#
#     left=s[:split]
#     right=s[split:]
#
#     score=left.count('0')+right.count('1')
#     maxcount=max(maxcount,score)
#     split +=1
# print(maxcount)
