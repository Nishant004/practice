# tokens = ["2","1","+","3","*"]
# tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# tokens =["4","3","-"]
tokens = ["3","11","5","+","-"]

stack = []

for i in tokens:
    if i == '-':
        val1 = stack[-1]
        val2 = stack[-2]
        stack.pop(-1)
        stack.pop(-1)
        stack.append(val2 - val1)
    elif i == '*':
        val1 = stack[-1]
        val2 = stack[-2]
        stack.pop(-1)
        stack.pop(-1)
        stack.append(val1 * val2)
    elif i == '+':
        val1 = stack[-1]
        val2 = stack[-2]
        stack.pop(-1)
        stack.pop(-1)
        stack.append(val1 + val2)
    elif i == '/':
        val1 = stack[-1]
        val2 = stack[-2]
        stack.pop(-1)
        stack.pop(-1)
        stack.append (int(val2 / val1))
        print(stack)
    else:
        stack.append(int(i))
print (sum(stack))