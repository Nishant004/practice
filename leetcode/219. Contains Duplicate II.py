# nums =[4,1,2,3,1,5]
# k = 3

# nums =[0,1,2,3,4,0,0,7,8,9,10,11,12,0]
# k =1

# nums =[313,64,612,515,412,661,244,164,492,744,233,579,62,786,342,817,838,396,230,79,570,702,124,727,586,542,919,372,187,626,869,923,103,932,368,891,411,125,724,287,575,326,88,125,746,117,363,8,881,441,542,653,211,180,620,175,747,276,832,772,165,733,574,186,778,586,601,165,422,956,357,134,857,114,450,64,494,679,495,205,859,136,477,879,940,139,903,689,954,335,859,78,20]
# k =22
nums = [1,2,3,1,2,3]
k = 2

dict1={}

for i in range(len(nums)):
    if nums[i] not in dict1:
        dict1[nums[i]]=[i]
    else:
        dict1[nums[i]].append(i)
        # dict1[nums[i]] += [i]
print(dict1)
for value in dict1.values():
    le=len(value)
    i=0
    if le >= 2:
        for i in range (0,len(value)-1):
            n = abs(value[i]-value[i+1])
            # print(n)
            if k >=n:

                print("True")
print("false1")


        # n = abs(value[i] - value[i + 1])
        # i +=1







        # print(value)

        # print(le)

        # for i in range (0,len(value)-1):
        #     n = abs(value[i]-value[i+1])

# if k >= n:
#     print("true")
# else:
#     print("false")











