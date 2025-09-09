# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        st = []
        while curr:
            st.append(curr.val)
            curr = curr.next

        curr = head
        while st:
            curr.val = st.pop()
            curr = curr.next
        return head

        