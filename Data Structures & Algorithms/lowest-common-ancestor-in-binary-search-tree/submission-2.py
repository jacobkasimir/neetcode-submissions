# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [root]

        while stack:
            cur = stack.pop()
            if cur.val < p.val and cur.val < q.val:
                stack.append(cur.right)
            elif cur.val > p.val and cur.val > q.val:
                stack.append(cur.left)
            else:
                return cur
            
