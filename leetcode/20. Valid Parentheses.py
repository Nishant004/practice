# s = "{()}"
# close={")" : "(" , "]" : "[" , "}" : "{" }

stack=[]

# for i in s:
#     if i in close:
#         if stack and stack[-1] == close[i]:
#             stack.pop()
#         else:
#             print("False")
#     else:
#         stack.append(i)
# print ("True2") if not stack else print("False2")

s = "{()}"
close={")" : "(" , "]" : "[" , "}" : "{" }
for p in s:
    if p in close.values():
        stack.append(p)
        print(stack)
    elif stack and close[p]==stack[-1]:
        stack.pop()
    else:
        print("False")
if stack==[]:
    print("true")
else:
    print("false")


# close={"(":")","{":"}","[":"]"}
# s = "{()}"
# for symbol in s:
#     if symbol in close.keys():
#         stack.append(symbol)
#         print(stack)
#     elif stack == [] or symbol != close[stack.pop()]:
#         print("false")
# print(stack)
# if stack==[]:
#    print("true")
# else:
#     print("False")