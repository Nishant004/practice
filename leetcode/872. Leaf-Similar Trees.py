# BFS
root1 = [3, 5, 1, 6, 2, 9, 8, null, null, 7, 4]
root2 = [3, 5, 1, 6, 7, 4, 2, null, null, null, null, null, null, 9, 8]


def tra(root,data):
    if not root:return
    if not root.left and not root.right :
        data.append(root.val)
        return
    tra(root.left, data)
    tra(root.right, data)

data1, data2 = [],[]

tra(root1,data1)
tra(root2,data2)

return data1==data2