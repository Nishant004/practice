ops = ["5","2","C","D","+"]

stack=[]

for i in ops:
    if i == 'D':
        stack.append(2*stack[-1])
    elif  i == 'C':
        stack.pop()
    elif i == '+':
        stack.append(stack[-1] + stack[-2])
    else:
        stack.append(int(i))
    print(stack)
print(sum(stack))


# stack = []
# for i in ops:
#     if i == 'D':
#         stack.append(2 * stack[-1])
#     elif i == 'C':
#         stack.pop()
#     elif i == '+':
#         stack.append(stack[-1] + stack[-2])
#     else:
#         stack.append(int(i))
# print( sum(stack))
