# nums = [10,9,2,5,3,7,101,18]

nums = [4,10,4,3,8,9]

# nums = [0,1,0,3,2,3]


stack=[]

for num in nums:
    if not stack or num > stack[-1]:
        stack.append(num)
        continue
    res = len(stack) - 1
    l,r = 0,res
    while l<= r:
        p = (l+r) // 2
        if stack[p] >= num:
            res=p
            r=p-1
        else:
            l=p+1
    stack[res] = num
print(len(stack))

