# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newnode = TreeNode(val)
        if root is None:
            return newnode
        curr = root
        while curr:
            if val < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = newnode
                    break
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = newnode
                    break
        return root
        