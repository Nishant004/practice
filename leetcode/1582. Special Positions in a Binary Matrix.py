# mat = [[1,0,0],[0,0,1],[1,0,0]]

mat = [[1,0,0],[0,1,0],[0,0,1]]

# mat=[[0,0,0,1],[1,0,0,0],[0,1,1,0],[0,0,0,0]]

# mat=[[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,1],[0,0,0,0,1,0,0,0],[1,0,0,0,1,0,0,0],[0,0,1,1,0,0,0,0]]


def get_column_sum(col_idx):
    # print(col_idx)
    # # print(get_column_sum())
    # print(row[col_idx] )
    return sum(row[col_idx] for row in mat)

count=0
for row in mat:
    if sum(row) == 1:
        col_idx=row.index(1)
        # print(col_idx)
        # print(row)
        count +=get_column_sum(col_idx)==1
        # print(count)
print (count)



# count=0
# list1={}
# for i in range(len(mat)):
#     # print(mat[i])
#     for j in range(len(mat[i])):
#         if mat[i][j]==1:
#             if j not in list1.values():
#                 count += 1
#                 list1[i] = j
#             if i not in list1.keys():
#                     # print(list1)
#             else:
#                     count -=1
#
# print(count)