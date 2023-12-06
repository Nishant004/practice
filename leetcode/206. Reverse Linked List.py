class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.head = None
    def reverseList(self, head):
            new_list=None
            current=head
            while current:
                new_node=current.next
                current.next=new_list
                new_list=current
                current=new_node
            return new_list

ne=ListNode()
sol=Solution()



