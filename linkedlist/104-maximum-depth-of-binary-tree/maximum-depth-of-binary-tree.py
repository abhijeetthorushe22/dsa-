# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is  None:
            return 0
        queue = [root]
        next_queue = []
        level = []
        result = []
        while queue :
            for root in queue:
                level.append(root.val)
                if root.left is not None:
                    next_queue.append(root.left)
                if root.right is not None:
                    next_queue.append(root.right)
            result.append(level)
            queue = next_queue
            next_queue = []
            level = []
            
        return len(result)
        