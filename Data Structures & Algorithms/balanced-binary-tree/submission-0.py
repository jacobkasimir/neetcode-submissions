class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(node):
            if not node:
                return 0
            
            left_height = get_height(node.left)
            if left_height == -1:
                return -1

            right_height = get_height(node.right)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1

            return 1 + max(left_height, right_height)
        
        return get_height(root) != -1

            