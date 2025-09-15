# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        num1 = ""
        num2 = ""
        while curr1:
            num1 += str(curr1.val)
            curr1 = curr1.next
        while curr2:
            num2 += str(curr2.val)
            curr2 = curr2.next


        num1real = num1[::-1]
        num2real = num2[::-1]
        number = int(num1real) + int(num2real)
        resultasstring = str(number)[::-1]
        #print(resultasstring)
        dummy = ListNode(int(resultasstring[0]))
        for i in range(1,len(resultasstring)):
            NewNode = ListNode(int(resultasstring[i]))
            if dummy is None:
                dummy = NewNode
            else:
                last = dummy
                while last.next is not None:
                    last = last.next
                last.next = NewNode
        return dummy

        
        

        





