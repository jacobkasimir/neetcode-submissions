class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        res = []

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                cur = queue.popleft()

                if cur.left:
                    queue.append(cur.left)

                if cur.right:
                    queue.append(cur.right)

                if i == level_size - 1:
                    res.append(cur.val)

        return res