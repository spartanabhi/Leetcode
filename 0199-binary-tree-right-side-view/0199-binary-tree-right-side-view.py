class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            result.append(queue[-1].val)

            level = []
            for node in queue:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)

            queue = level

        return result