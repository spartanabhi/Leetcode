class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_leaves_sum = 0
        q = collections.deque([root])
    
        while q:
            node = q.popleft()

            # Check if the left child exists
            if node.left:
                # Check if this left child is a LEAF node
                if not node.left.left and not node.left.right:
                    left_leaves_sum += node.left.val
                else:
                    # If it's not a leaf, push it to the queue to explore later
                    q.append(node.left)
            
            # Right children are pushed to the queue to explore, 
            # but they can never be left leaves themselves.
            if node.right:
                q.append(node.right)
                
        return left_leaves_sum
