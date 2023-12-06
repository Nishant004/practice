nums = [4,1,2,1,2]

newnums=0
res=[]
for i in nums:
    newnums ^= (i)
res.append(newnums)
print (res)