f=flowerbed =[0,1,0,0,1]
n=1
# [1,0,0,0,0,0,1]
# [0,0,1,0,1]
# n = 1
# count=0
#
# if n==0:
#     print("True1")
# for i in range(len(flowerbed)):
#     if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
#         flowerbed[i] = 1
#         count += 1
# print(count)
prev,count=0,0
for cur in flowerbed:
    if cur !=0  :
        if prev != 0:
            count-=1
        prev=1
    else:
        if prev != 0:
            prev=0
        else:
            count+=1
            prev=1
print( count>=n)
# if n == 0:
#     return True
# for i in range(len(flowerbed)):
#     if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
#         flowerbed[i] = 1
#         n -= 1
#         if n == 0:
#             return True
# return False




