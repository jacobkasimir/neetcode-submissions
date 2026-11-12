# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [root]
        m = root.val

        while stack:
            cur = stack.pop()
            if cur.val < p.val and cur.val < q.val:
                stack.append(cur.right)
                m = cur.right.val
            elif (cur.val < p.val and cur.val == q.val) or (cur.val < q.val and cur.val == p.val):
                return cur
            elif cur.val > p.val and cur.val > q.val:
                stack.append(cur.left)
                m = cur.left.val
            else:
                return cur
            
