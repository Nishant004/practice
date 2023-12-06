list1 = [1,2,4]
list2 = [1,3,4]

# ls = list1+list2
#
# print(sorted(ls))

dummy = ListNode()
head = dummy

while list1 and list2:
    if list1.val <= list2.val:
        head.next = list1
        list1 = list1.next
    else:
        head.next = list2
        list2 = list2.next
    head = head.next

if list1:
    head.next = list1
elif list2:
    head.next = list2

return dummy.next