# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        if not arr:
            return None

        
        arr.sort()
        
        head = ListNode(arr[0])
        temp = head
        for val in arr[1:]:

            temp.next = ListNode(val)
            temp = temp.next
        return head
        