prices = [7,1,5,3,6,4]
pro=0
b=prices[0]
for s in prices[1:]:
    if s > b:
        pro=max(pro,s-b)
    else:
        b=s
print(pro)