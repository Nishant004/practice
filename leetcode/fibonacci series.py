

a=0
b=1
c=0

digit=int(input("Enter number:"))

for i in range(0,digit):
    c=a+b
    a=b
    b=c
    print(b)