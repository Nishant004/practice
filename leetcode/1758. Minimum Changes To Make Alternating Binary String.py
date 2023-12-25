class Solution:
    def counts(string, new_string) -> int:
        count = 0
        for i in range(len(string)):
            if string[i] != new_string[i]:
                count += 1
        return count

    # string convert start from 1  example 101010101
    def string1(string: str):
        new_string = ''
        for i in range(len(string)):
            if i % 2 == 0:
                new_string += '1'
            else:
                new_string += '0'

        return (counts(string, new_string))

    # string function start from 0
    def string2(string):
        new_string = ''
        for i in range(len(string)):
            if i % 2 == 0:
                new_string += '0'
            else:
                new_string += '1'
        return count(string, new_string)
    def minOperations(self, string: str) -> int:

        return (min(string1(string), string2(string)))




obj=Solution()
obj.minOperations('0100')




























# s = "0100"
# s ="1111"
# s ="0110101010"
# s="110010"
# s='10'
# s="101101111"
# s ="10010100"

# start1 = 0
# start0 = 0
#
# for i in range(len(s)):
#     if i % 2 == 0:
#         if s[i] == "0":
#             start0 += 1
#         else:
#             start1 += 1
#     else:
#         if s[i] == "1":
#             start0 += 1
#         else:
#             start1 += 1
# print(min(start1, start0))

# start0 = 0
#
# for i in range(len(s)):
#     if i % 2 == 0:
#         if s[i] == "1":
#             start0 += 1
#     else:
#         if s[i] == "0":
#             start0 += 1
#
# return min(start0, len(s) - start0)

















# s = "0100"
# s ="1111"
# s ="0110101010"
# s="110010"
# s='10'
# s="101101111"
# s ="10010100"


#
#
# EEN=0
# EOD=0
# OEN=0
# OOD=0
#
#
# for i in range(len(s)):
#     if i % 2 == 0:
#         if s[i] == "0":
#             EEN +=1
#         else:
#             EOD +=1
#
#     if i % 2 ==1:
#         if s[i] == "1":
#             OOD +=1
#         else:
#             OEN +=1

# print(EEN,EOD)
# print(OEN,OOD)
# if EEN == OOD and EEN > 0 and OOD > 0 :
#     print(EEN+OOD)
# elif EEN == OOD:
#     print('0')
# else:
#     if OEN > EOD:
#         print(OEN)
#     else:
#         print(EOD)

# print((OEN+EOD)+(EEN+OOD))
# if EEN==OOD :
#     print(0)
# else:
#     print(OEN+EOD)