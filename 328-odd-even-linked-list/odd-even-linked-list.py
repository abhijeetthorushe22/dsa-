# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        arr = []
        temp = head
        while temp and temp.next:
            arr.append(temp.val)
            temp=temp.next.next
        if temp :
            arr.append(temp.val)
        temp = head.next
        while temp and temp.next:
            arr.append(temp.val)
            temp=temp.next.next
        if temp :
            arr.append(temp.val)
        head = ListNode(arr[0])
        curr = head
        for val in arr[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head

        

        
         
        