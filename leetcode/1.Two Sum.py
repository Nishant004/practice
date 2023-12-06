nums = [11,7,15,2]
target = 9

n =len(nums)

for i in range(n):
    second_no=target-nums[i]
    for j in range(i+1 ,n):
        if second_no==nums[j]:

            print (i,j)

