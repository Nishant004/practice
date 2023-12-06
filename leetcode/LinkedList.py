class Node: #step2(n1 , 1)
    def __init__(self,data):
        self.data=data  #step2 n1=1,      step6 n2=2
        self.next=None  #n1.next=None     n2.next=None
        print("Node1")
class SLL:
    def __init__(self):
        self.head=None  #step4 pass here (sll.head=None)
        print("Node2")
    def traverse(self):
        if self.head is None:
            print("List is Empty")
        else:
            list=self.head  #sll.head=n1 not empty
            while list is not None:
                print(list.data, end=" ")
                list=list.next

#Insert At the beginning

    def insert_at_beg(self,data):
        ATB=Node(data)
        ATB.next=self.head # jo hai (sll.head) jo hai (n1)
        self.head=ATB # (self.head) jo starting point tha (n1) change to ATB

#Insert At the End

    def at_end(self,data):
        ATE=Node(data)
        nakliHead=self.head # nakli head to traverse kare loop mia end tak
        while nakliHead.next is not None :
            nakliHead = nakliHead.next
        nakliHead.next =ATE

#Insert in Between

    def in_between(self,position,data):
        nib=Node(data)
        a=self.head
        for i in range(1,position-1):
            a=a.next
            nib.next=a.next
            a.next=nib
#Delete from Bignning
    def del_beg(self):
        print()
        temp=self.head
        self.head=temp.next
        temp.next=None
    def del_end(self):
        print()
        pre=self.head
        nex=self.head.next
        while nex.next is not None:
            pre=pre.next
            nex=nex.next
        pre.next=None
    def del_betw(self,position):
        print()
        pre=self.head
        nex=self.head.next
        for i in range(1,position-1):
            nex=nex.next
            pre=pre.next
        pre.next=nex.next
        nex.next=None
    def reverseList(self):
        print()
        current = self.head
        new_list=None

        print("reverse")
        while current:
            self.head = new_list
            new_node=current.next
            current.next=new_list
            new_list=current
            current=new_node
        return new_list


n1=Node(1)   #step 1 object is created
sll=SLL()    #step 3 object is created 'sll'
sll.head=n1  #step 5 sll point to n1
n2=Node(2)   #step 6 create
n1.next=n2   #step 7 connect n1.next to n2
n3=Node(3)
n2.next=n3
sll.traverse()  # call object SLL class == sll
sll.insert_at_beg(7)
sll.traverse()
sll.at_end(20)
sll.traverse()
sll.in_between(3,7)
sll.traverse()
# sll.del_beg()
# sll.traverse()
# sll.del_end()
# sll.traverse()
# sll.del_betw(3)
# sll.traverse()
print(sll.reverseList())
sll.traverse()
