# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        sp, sq = [p], [q]

        while sp and sq: 
            pv, qv = sp.pop(), sq.pop()
            if not pv.val == qv.val:
                return False
            
            if pv.left and qv.left:
                sp.append(pv.left)
                sq.append(qv.left)
            elif pv.left or qv.left:
                return False
            
            if pv.right and qv.right:
                sp.append(pv.right)
                sq.append(qv.right)
            elif pv.right or qv.right:
                return False
            
            
        
        return True
