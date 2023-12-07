n = 70
used=[]

while n > 0 :
    storge=0
    while n>0:
        temp = n % 10
        storge += temp ** 2
        n = n // 10

    if (storge in used):
        #print("False")
        pass
    else:
        used.append(storge)
        print(storge)
        print(used)
    if (storge == 1):
        pass
        #print("True")

    n = storge


#print("False")







