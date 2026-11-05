# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        if root.left or root.right:
            d = root.right if root.right else None
            root.right = root.left if root.left else None
            root.left = d

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
