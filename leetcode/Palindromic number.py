no=4004
new_no=no
reminder=0

while(new_no > 0):
    digit=new_no%10
    reminder=reminder*10+digit
    new_no=new_no//10

    print(reminder)
