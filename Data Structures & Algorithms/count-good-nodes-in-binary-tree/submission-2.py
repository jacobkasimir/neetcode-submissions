class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        stack = [(root, root.val)]

        while stack:
            cur, max_val = stack.pop()

            if cur.val >= max_val:
                good += 1

            max_val = max(max_val, cur.val)

            if cur.left:
                stack.append((cur.left, max_val))

            if cur.right:
                stack.append((cur.right, max_val))

        return good

        