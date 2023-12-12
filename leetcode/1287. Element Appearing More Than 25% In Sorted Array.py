# arr = [1,2,2,6,6,6,6,7,10]
arr = [1,1]

dict1={}

for i in arr:
    if i in dict1:
        dict1[i] +=1
    else:
        dict1[i] =1
    if dict1[i] > (len(arr)//4):
        print(i)
