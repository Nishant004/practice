heights = [1,1,4,2,1,3]
sh=sorted(heights)
count=0
for i in range(len(heights)):
    if heights[i] != sh[i]:
        count +=1
        i +=1
print(count)