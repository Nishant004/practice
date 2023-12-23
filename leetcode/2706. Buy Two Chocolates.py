# prices = [3,2,3]
prices=[1,2,2]
money = 3
prices.sort()
count=2
i=0

while count > 0:
    s = money - prices[i]
    # print(s)
    if s >= prices[i+1]:
        s=s-prices[i+1]
       
    else:
        break
print(money)