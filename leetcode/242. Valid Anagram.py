s = "anagram"
t = "nagaram"


if len(s)>len(t):
    print("False")

dict1={}

for i in s:
    if i in dict1:
        dict1[i] +=1
    else:
        dict1[i] = 1

for aphabet in t:
    if aphabet not in dict1:
        print("False")
    if dict1[aphabet]<=0:
        print("False")

    dict1[aphabet] -=1
print("true")