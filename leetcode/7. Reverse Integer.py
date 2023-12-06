x = 1534236469
# count=0
#
# if x<0:
#     x *=-1
#     while x>0:
#         temp=x%10
#         count=count*10+temp
#         x=x//10
#     count *=-1
# else:
#     while x>0:
#         temp=x%10
#         count=count*10+temp
#         x=x//10
# if count>(2**31)-1 or count<-(2**31):
# print (count)

# class Solution:
#     def reverse(self, x: int) -> int:
count = 0

if x < 0:
    x *= -1
    while x > 0:
        temp = x % 10
        count = (count * 10) + temp
        x //= 10

    count *= -1

else:
    while x > 0:
        temp = x % 10
        count = (count * 10) + temp
        x //= 10


if count > (2 ** 31) - 1 or count < -(2 ** 31):
    print(0)
else:
    print (count)
