nums =[9,6,4,2,3,5,7,0,1]
n=len(nums)
temp=0
i=0
sum=0

for j in range(n):
     sum= sum +nums[j]
while i <= n:
     temp = temp + i
     i +=1
temp = temp - sum
print(temp)


