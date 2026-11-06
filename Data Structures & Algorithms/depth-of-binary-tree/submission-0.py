# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0 if not root else 1

        if not root:
            return res
        
        return res + max(self.maxDepth(root.left), self.maxDepth(root.right))