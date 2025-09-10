# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        slow = fast = head  

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        curr = slow
        prev = None
        while curr:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
        
        while head and prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
           
        
        return True
        
            

        
        
        