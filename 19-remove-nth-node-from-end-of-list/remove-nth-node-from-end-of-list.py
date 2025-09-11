# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        
        
        
        count = 0
        temp = head
        while temp:
            count+=1
            temp = temp.next
        if count == n:
            return head.next
        count1 = count-n
        
        temp = head
        
        count2 = 0
        while temp:
            count2+=1
           
            if count2==count1:
                temp.next = temp.next.next
           
            
           
            temp = temp.next
        
        return head

        