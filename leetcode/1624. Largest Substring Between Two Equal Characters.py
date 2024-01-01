# s = "aa"
s = "cbzxy"
s = "axyzabcya"
# s="abca"

dict1={}
max_val=-1

for i in range(len(s)):
    if s[i] not in dict1:
        dict1[s[i]] = [i]
    else:
        dict1[s[i]] += [i]
    for val in dict1.values():
        if len(val) > 1:
            max_val=max(max_val,val[len(val)-1]-val[0]-1)
print(max_val)





