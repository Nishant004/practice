path = "NESW"

dict1={
    'N' : [0,1],
    'S' :[0,-1],
    'E' :[1,0],
    'W':[-1,0]
}

vis = set()
x=0
y=0

for i in path:
    vis.add((x,y))

    xd , yd = dict1[i]
    print(xd, yd, "d")
    x,y = x + xd ,y + yd
    print(x ,y ,"xy")


    if (x,y) in vis:
        print("true")
print('False')

#         x, y = 0, 0
#         visited = set()
#         visited.add((0, 0))
#
#         for direction in path:
#             if direction == 'N':
#                 y += 1
#             elif direction == 'S':
#                 y -= 1
#             elif direction == 'E':
#                 x += 1
#             else:
#                 x -= 1
#
#             current_pos = (x, y)
#             if current_pos in visited:
#                 return True  # Path crosses itself
#             else:
#                 visited.add(current_pos)
#
#         return False  # Path does not cross itself
#
