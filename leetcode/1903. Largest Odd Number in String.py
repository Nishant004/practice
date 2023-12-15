num = "542469"
s=0
n=len(num)

# for i in range(len(num) - 1, -1, -1):
#     if int(num[i]) % 2 == 1:
#         print( num[:i + 1])
#
# print("")


for i in range(len(num)-1,-1,-1):
    # if int(num[n-1])%2 == 1:
    #     print(num)
    if int(num[i])%2==1:
        print(num[:i+1])
print("even")

# one  line answer  rstrip funcion
# return num.rstrip("02468")



    # if int(numnum[i][i] )



