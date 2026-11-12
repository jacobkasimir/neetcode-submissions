# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        elif not (root.left or root.right):
            return [[root.val]]
        
        stack = deque([root])
        h = deque([0])
        ch = 0
        res = [[]]

        while stack:
            cur = stack.popleft()
            if ch == h.popleft():
                res[ch].append(cur.val)
            else:
                ch = ch + 1
                res.append([])
                res[ch].append(cur.val)
            
            if cur.left:
                stack.append(cur.left)
                h.append(ch + 1)
            if cur.right:
                stack.append(cur.right)
                h.append(ch + 1)

        return res
            