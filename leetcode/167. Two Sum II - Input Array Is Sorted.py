numbers = [2,7,11,15]
target = 9

# numbers = [2,3,4]
# target = 6

# numbers = [-1,0]
# target = -1

high = len(numbers) - 1
i = 0
# while i < high:
#     if target == numbers[i] + numbers[high]:
#         print ((i + 1), (high + 1))
#     elif target < numbers[i] + numbers[high]:
#         high -= 1
#     else:
#         i += 1

while i < high:
    two_Sum = numbers[i] + numbers[high]

    if two_Sum > target:
        high -= 1

    elif two_Sum < target:
        i += 1

    else:
        print (i + 1, high + 1)